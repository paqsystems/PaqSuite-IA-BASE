import os
import re
import time
from urllib.parse import urljoin, urldefrag, urlparse

import requests
from bs4 import BeautifulSoup
import html2text


SEED_URLS = [
    "https://ayudas.axoft.com/25ar/documentos/",
]

ALLOWED_PREFIXES = [
    "https://ayudas.axoft.com/25ar/documentos/",
]

OUTPUT_DIR = "axoft_md/25ar/"
MAX_PAGES = 35000
PAUSE_SECONDS = 1
MIN_URL_DEPTH = 5

def safe_folder_name(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]+', "-", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name[:80] or "GENERAL"
    
def url_depth(url: str) -> int:
    path = urlparse(url).path.strip("/")
    return len([p for p in path.split("/") if p])

def normalize_url(url: str) -> str:
    url, _fragment = urldefrag(url)
    url = url.strip()

    if url.endswith("/"):
        return url

    return url + "/"


def is_allowed(url: str) -> bool:
    return any(url.startswith(prefix) for prefix in ALLOWED_PREFIXES)


def safe_filename(title: str, url: str) -> str:
    if not title:
        title = urlparse(url).path.strip("/").replace("/", " - ")

    name = re.sub(r'[\\/:*?"<>|]+', "-", title)
    name = re.sub(r"\s+", " ", name).strip()
    return name[:150] + ".md"


def fetch_html(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36",
        "Accept-Language": "es-AR,es;q=0.9,en;q=0.8",
    }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    return response.text


def extract_links(html: str, base_url: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"].strip()

        if href.startswith(("mailto:", "tel:", "javascript:", "#")):
            continue

        absolute = normalize_url(urljoin(base_url, href))

        if is_allowed(absolute):
            links.add(absolute)

    return sorted(links)


def extract_main_content(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "html.parser")

    title_tag = soup.find("h1") or soup.find("title")
    title = title_tag.get_text(" ", strip=True) if title_tag else "Sin título"

    # El contenido principal del sitio aparece dentro de <main class="content">
    main = soup.find("main", class_="content")

    if not main:
        main = soup.find("main")

    if not main:
        main = soup.body or soup

    # Quitar elementos poco útiles
    for tag in main.find_all(["script", "style", "nav", "footer", "form"]):
        tag.decompose()

    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = True
    converter.body_width = 0

    markdown = converter.handle(str(main)).strip()

    return title, markdown


def detectar_metadata(url: str):
    version = "Desconocida"
    modulo = "General"
    categoria = "General"

    if "/24ar/" in url:
        version = "24AR"

    if "/25ar/" in url:
        version = "25AR"

    if "/guias/" in url:
        categoria = "Guía"

    if "/operacion/" in url:
        categoria = "Operación"

    modulos = {
        "_gv": "Ventas",
        "_cp": "Compras",
        "_st": "Stock",
        "_sb": "Tesorería",
        "_sua": "Sueldos",
        "_afa": "Activo Fijo",
        "_cont": "Contabilidad",
    }

    for clave, nombre in modulos.items():
        if clave in url:
            modulo = nombre
            break

    return version, modulo, categoria
def save_markdown(title: str, url: str, content: str):
    version, modulo, categoria = detectar_metadata(url)

    modulo_limpio = safe_folder_name(modulo.upper())

    carpeta_modulo = os.path.join(OUTPUT_DIR, modulo_limpio)
    os.makedirs(carpeta_modulo, exist_ok=True)

    filename = safe_filename(f"[{modulo_limpio}] {title}", url)
    path = os.path.join(carpeta_modulo, filename)

    if os.path.exists(path):
        print(f"YA EXISTE: {path}")
        return

    md = f"""# {title}

## Metadata

- Producto: Tango
- Version: {version}
- Modulo: {modulo}
- Categoria: {categoria}
- URL: {url}

## Contenido

{content}
"""

    with open(path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"Guardado: {path}")

def crawl():
    queue = [normalize_url(url) for url in SEED_URLS]
    visited = set()
    processed = 0

    while queue and processed < MAX_PAGES:
        url = queue.pop(0)

        if url in visited:
            continue

        if not is_allowed(url):
            continue

        print(f"Procesando: {url}")

        try:
            html = fetch_html(url)
            visited.add(url)

            depth = url_depth(url)

            if depth >= MIN_URL_DEPTH:
                title, markdown = extract_main_content(html)
                save_markdown(title, url, markdown)
            else:
                print(f"IGNORADA (índice): {url}")

            links = extract_links(html, url)
            print(f"Links encontrados: {len(links)}")

            for link in links:
                if link not in visited and link not in queue:
                    queue.append(link)

            print(f"Pendientes: {len(queue)}")
            processed += 1
            time.sleep(PAUSE_SECONDS)

        except Exception as e:
            print(f"ERROR en {url}: {e}")

    print(f"\nFinalizado. Páginas procesadas: {processed}")

    if processed >= MAX_PAGES and queue:
        print(
            f"Motivo: se alcanzó MAX_PAGES ({MAX_PAGES}). "
            f"Enlaces pendientes sin procesar: {len(queue)}."
        )
    elif not queue:
        print("Motivo: no quedan enlaces pendientes en la cola (recorrido completo).")
    else:
        print(
            f"Motivo: se alcanzó MAX_PAGES ({MAX_PAGES}) y la cola quedó vacía."
        )


if __name__ == "__main__":
    crawl()