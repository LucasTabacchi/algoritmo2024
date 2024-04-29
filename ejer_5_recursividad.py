def usar_la_fuerza(mochila, objetos_sacados=0):
    if len(mochila) == 0:
        return False, objetos_sacados
    
    objeto = mochila.pop(0)
    if objeto == 'sable de luz':
        return True, objetos_sacados + 1
    else:
        return usar_la_fuerza(mochila, objetos_sacados + 1)

mochila_jedi = ['botiquín', 'diccionario', 'agua', 'auto', 'computadora','sable de luz','mesa']
print(usar_la_fuerza(mochila_jedi))