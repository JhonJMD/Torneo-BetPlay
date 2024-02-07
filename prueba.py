# Definimos una lista de listas
lista_externa = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]

# Definimos la posición de la lista interna que queremos modificar
posicion_lista_interna = 1  # Por ejemplo, queremos modificar la segunda lista interna

# Definimos el índice del atributo que queremos modificar dentro de la lista interna
indice_atributo = 1  # Por ejemplo, queremos modificar el segundo elemento de la lista interna

# Nuevo valor para el atributo
nuevo_valor = "X"

# Modificamos el atributo deseado
lista_externa[0][2] = nuevo_valor

# Mostramos la lista modificada
print(lista_externa)
