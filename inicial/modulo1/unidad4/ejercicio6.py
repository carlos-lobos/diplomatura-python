# 1ra Forma (usando funcion provista por python)
def ordenar_lista(lista):
    lista.sort()
    print(lista)

# 2da Forma (usando funcion con algoritmo propio - menos performante)
def ordenar_lista_2(lista):
    changed = True
    while changed:
        changed = False
        for i in range(0, len(lista)-1):
            if lista[i] > lista[i+1]:
                changed = True
                mayor = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = mayor
    print(lista)


lista = [3, 44, 21, 78, 5, 56, 9]
ordenar_lista(lista)

lista = [3, 44, 21, 78, 5, 56, 9]
ordenar_lista_2(lista)
