comparto la selección.
agregaría los tres atributos "agregadosErroneos", "ModificadosErroneos" y "eliminadosErroneos", de este modo, los 6 atributos deben sumar el total procesado.
en el get, mientras no sea el resultado final, devolvería todos los valores en null (no devolvería resultados provisorios), más allá que internamente convenga ir actualizando la tabla.
no me molesta conservar los json aunque compliquen o demoren el proceso posterior. cuanto más rápido sean los endpoints de envió de información,mejor.
confirmaciones:
1. el identificador lo genera el ERP.
2. usar UltimoEnvio
3. se permite snapshot vacío
4. bajas : físicas. las inhabilitaciones son modificando el atributo, si lo tienen.
5. se acepta resultado eventual 202.
6. explícamelo en lenguaje humano.
7. preferiría detalle de errores completo. el temor es si es demasiado grando. pero empecemos así
8. explícamelo en lenguaje humano.
9. cuáles son las sugerencias según las mejores prácticas?
10. procuraría evitarla. en ese caso, cuando la segunda concurrencia envia el primer juego de datos, si se ve uno en proceso para ese recurso, devolver error. El ERP debe saber que ante un error debe cortar el envió de los siguientes lotes, si hubiere, y avisar al usuario (o registrar error si el proceso es automatizado)

otros temas:
1) adecuar los archivos para postman agregando los nuevos atributos, en los json existentes, y un endpoint para el get de consulta de resultado
2) Sugiero que procesemos en etapas, del modo : 
a) probar primero conel endpoint de "condiciones de venta", que es una sola pasada.
b) después con el endpoint de artículos.
c) Aprobados a) y b), haría todo el resto conjuntamente.
d) Modificar el endpoiint de clientes. Direcciones de entrega y contactos se deben resolver conjuntamente, llevando la información como nodos hijos de los clientes.
