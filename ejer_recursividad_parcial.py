def listar_inversa(lista):
    if len(lista) == 0:
        return None
    else:
        print(lista[-1], end=' ')
        listar_inversa(lista[:-1])


mi_lista = [1, 2, 3, 4, 5]
listar_inversa(mi_lista)
