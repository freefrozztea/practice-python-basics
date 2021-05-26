def ordenarCadena(cadena):
    lista = [x for x in cadena if x != " "]

    return lista


# Programa principal

cadenita = "Tengo hambre no se me ocurre nada"
print(ordenarCadena(cadenita))
