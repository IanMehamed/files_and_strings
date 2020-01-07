# Este programa recorre un archivo en busca de un string, y en caso de encontrarlo,
# muestra el texto con otro string agregado inmediatamente a continuacion.

archivo = open('texto.txt','r')
texto = archivo.read()
palabra_buscada = "cuarta"
posicion = texto.find(palabra_buscada)
if posicion == -1:
    print('No se encontro la palabra\n')
else:
    texto_agregado = ' (Cuarta viene del numero 4) '
    nuevo_texto = texto[:posicion + len(palabra_buscada)] + texto_agregado + texto[posicion + len(palabra_buscada):]
    print(nuevo_texto)
archivo.close()
