# Desarrollar una función que determine si una cadena de caracteres es capicúa, sin utilizar cadenas auxiliares ni rebanadas
# Escribir además un programa que permita verificar su funcionamiento


def esCapicua(cadena):
    maximo = len(cadena)
    flag = True
    for i in range(0, maximo // 2):
        if cadena[i].lower() != cadena[-(1 - i)].lower():
            print(cadena[i].lower())
            print(cadena[-(1 - i)].lower())
            flag = False
            break

    return flag


def esCapicua2(cadena):
    lista = list(cadena)
    lista1 = [x.lower() for x in lista if (not x.isspace())]
    maximo = len(lista1)
    flag = True

    for i in range(0, maximo // 2):
        if lista1[i] != lista1[-(1 + i)]:
            flag = False
            print(lista1[i])
            print(lista1[-(1 + i)])
            break

    return flag


# Programa principal

cadena = "Anita lava la tina"
print(esCapicua(cadena))
print(esCapicua2(cadena))
