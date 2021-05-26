def eliminaSubcadenaRebanadas(cadena, posicion, cantidad):
    longitud = len(cadena)
    resp = cadena[posicion : (posicion + cantidad)]
    return resp


def eliminaSubcadenaSimple(cadena, posicion, cantidad):
    longitud = len(cadena)
    long2 = posicion + cantidad
    resp = ""
    for i in range(posicion, long2):
        if i > longitud - 1 or posicion < 0:
            break
        resp = resp + cadena[i]

    return resp


# Programa principal

cadena = "Alguna cosa"
posicion = -3
cantidad = 4
print(eliminaSubcadenaRebanadas(cadena, posicion, cantidad))
print(eliminaSubcadenaSimple(cadena, posicion, cantidad))
