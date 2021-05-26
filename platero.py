# Escribir un programa que cuente cuantas veces se encuentra una subcadena dentro de otra cadena, sin diferenciar mayúsculas y minúsculas.
# Tener en cuenta que los carácteres de la subcadena no necesariamente deben estar en forma consecutiva dentro de la cadena, pero sí
# respetando el orden de los mismos

# Mi pseudocódigo:
# defino funcion recibiendo como parámetros la cadena y la subcadena
#     Las convierto en minúsculas a ambas
#     Creo variable respuesta en 0
#     Luego busco el primer caracter - ver si uso find o alguna otra
#         Si está:
#             Busco el segundo viendo que el tercero o el cuarto no aparezcan antes
#                 Si es correcto:
#                     Busco el tercero viendo que el cuarto no aparezca antes
#                         Si es correcto:
#                             actualizo contador y renuevo la búsqueda desde el primero
#                         Si no es correcto:
#                             corto ciclo
#                 si no es correcto:
#                     corto ciclo

#     retorno respuesta


def busquedaLista(lista1, lista2):

    lista1Aux = lista1[::]
    lista2Aux = lista2[::]
    posAux = 0
    i = 0

    while True:

        if len(lista2Aux) == 0:
            break

        cadenaAux = "".join(lista1Aux)
        indice = cadenaAux.find(lista2Aux[0])

        if indice == -1:
            posAux = indice
            break

        lista1Aux = lista1Aux[indice + 1 :]
        posAux = posAux + indice + 1
        lista2Aux = lista2Aux[1:]

    # print(posAux)
    return posAux


def cantidadSubcadena(cadena, subcadena):
    listaCadena, listaSubcadena = list(cadena.lower()), list(subcadena.lower())
    respuesta = 0

    while len(listaCadena) > 0:
        if len(listaSubcadena) == 0:
            break
        pos = busquedaLista(lista1=listaCadena, lista2=listaSubcadena)
        if pos != -1:
            listaCadena = listaCadena[pos + 1 : :]
            respuesta = respuesta + 1

    return respuesta


# Programa principal

cadena = "Platero es pequeño peludo, suave; tan blando por fuera que se diría todo de algodón, \
que no lleva huesos. Sólo los espejos de azabache de sus ojos son duros cual dos escarabajos de cristal negro"
subcadena = "UADE"
# subcadena = "www"
# subcadena = ""
print(cantidadSubcadena(cadena=cadena, subcadena=subcadena))
