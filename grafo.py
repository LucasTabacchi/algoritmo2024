from cola import Queue
from heap import HeapMin
from pila import Stack

class Graph:
    def __init__(self, dirigido=True):
        self.elements = []
        self.dirigido = dirigido

    def show_graph(self):
        print()
        print("nodos")
        for index, nodo in enumerate(self.elements):
            print(nodo['value'])
            print(f"    aristas")
            for second_index, second_element in enumerate(nodo['aristas']):
                print(f'    destino {second_element['value']} peso: {second_element['peso']}')
        print()

    def search(self, value):  #Busca un nodo
        for index, element in enumerate(self.elements):
            if element['value'] == value:
                return index

    def search_arista(self, vertice_value, value): #busca un vértice y si lo encuentra accede a la lista de arista y busca el vértice 
        pos_origen = self.search(vertice_value)    # destino,si lo encuentra devuelve el vértice origen y la posición de la arista en
        if pos_origen is not None:                 #la lista de aristas
            for index, element in enumerate(self.elements[pos_origen]['aristas']):
                if element['value'] == value:
                    return pos_origen, index

    def insert_vertice(self, value, other_value=None):
        nodo = {
        'value': value,
        'aristas': [],
        'visitado': False,
        "other_value": other_value
        }
        self.elements.append(nodo)

    def insert_arista(self, origen, destino, peso):
        pos_origen = self.search(origen)
        pos_destino = self.search(destino)
        if pos_origen is not None and pos_destino is not None:
            # print(origen, destino)
            arista = {
                'value': destino,
                'peso': peso
            }
            self.elements[pos_origen]['aristas'].append(arista)   # agrega la arista a la lista de aristas del vertice_origen con el destino que va ser el vertice_destino
            if not self.dirigido:
                arista = {
                    'value': origen,
                    'peso': peso
                }
                self.elements[pos_destino]['aristas'].append(arista) #en el caso de ser no dirigido también agrega la arista a la lista de aristas del vertice_destino,
                                                                     # con la diferencia que el destino va ser el vertice_origen

    
    def delete_arista(self, origen, destino): #busca la arista y si existe la elimina de la lista de aristas del vétice origen, en el caso
        result = self.search_arista(origen, destino) #de que sea no dirigido también la elimina del vértice destino
        if result:
            pos_vertice, pos_arista = result
            value = self.elements[pos_vertice]['aristas'].pop(pos_arista)
            if not self.dirigido:
                result = self.search_arista(destino, origen)
                if result:
                    pos_vertice, pos_arista = result
                    self.elements[pos_vertice]['aristas'].pop(pos_arista)
            return value
    
    def delete_vertice(self, value):
        pos_vertice = self.search(value)
        if pos_vertice is not None:
            delete_value = self.elements.pop(pos_vertice)
            for nodo in self.elements:
                self.delete_arista(nodo['value'], value)  #recorre los nodos restantes (es decir, todos los vértices que no han
            return delete_value                           #sido eliminados aún) y elimina cualquier arista que conecte esos nodos
                                                          # con el vértice que se acaba de eliminar.
    
    def mark_as_not_visited(self):
        for nodo in self.elements:
            nodo['visitado'] = False

    def deep_show(self, origin):         #busca el vértice y si lo encuentra lo marca como visitado,imprime el valor y obtiene la
        def __deep_show(graph, origin):  #lista de los vértices adyacentes, despues recorre la lista y los muestra 
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    print(graph.elements[pos_vertice]['value'])
                    adyacentes = graph.elements[pos_vertice]['aristas']
                    for adyacente in adyacentes:   #una vez que obtenes lo adyacentes se llama devuelta internamente devuelta a la 
                        __deep_show(graph, adyacente['value'])  #función pero para cada uno de los nodos de la lista de adyacentes,
                                                                #accediendo a la key value de cada una de las aristas
        self.mark_as_not_visited()
        __deep_show(self, origin)

    def amplitude_show(self, origin):
        self.mark_as_not_visited()
        cola = Queue()
        pos_vertice = self.search(origin)
        if pos_vertice is not None:
            if not self.elements[pos_vertice]['visitado']:
                cola.arrive(self.elements[pos_vertice])
                while cola.size() > 0:
                    nodo = cola.attention()
                    nodo['visitado'] = True
                    print(nodo['value'])
                    adyacentes = nodo['aristas']
                    for adyacente in adyacentes:
                        pos_adyaecnte = self.search(adyacente['value'])
                        if not self.elements[pos_adyaecnte]['visitado']:
                            cola.arrive(self.elements[pos_adyaecnte])
    
    def exist_path(self, origen, destino):   #busca el nodo y si existe verifica si existe paso accediendo a la lista de adyacentes,cuando
        def __exist_path(graph, origin, destino): #se cumple que el nodo origen es igual al destino delvuelve True(significa que llegó al nodo y existe paso)
            result = False
            pos_vertice = graph.search(origin)
            if pos_vertice is not None:
                if not graph.elements[pos_vertice]['visitado']:
                    graph.elements[pos_vertice]['visitado'] = True
                    if graph.elements[pos_vertice]['value'] == destino:
                        return True
                    else:
                        adyacentes = graph.elements[pos_vertice]['aristas']
                        for adyacente in adyacentes:
                            result = __exist_path(graph, adyacente['value'], destino)
                            if result:
                                break
            return result
        
        self.mark_as_not_visited()
        result = __exist_path(self, origen, destino)
        return result

    def dijkstra(self, origen):
        from math import inf
        no_visitados = HeapMin()
        camino = Stack()
        for nodo in self.elements:
            distancia = 0 if nodo['value'] == origen else inf
            no_visitados.arrive([nodo['value'], nodo, None], distancia)
        while len(no_visitados.elements) > 0:
            node = no_visitados.atention()
            costo_nodo_actual = node[0]
            camino.push(node)
            adjacentes = node[1][1]['aristas']
            # print(costo_nodo_actual, adjacentes)
            for adjacente in adjacentes:
                pos = no_visitados.search(adjacente['value'])
                if pos is not None:
                    if costo_nodo_actual + adjacente['peso'] < no_visitados.elements[pos][0]:
                        no_visitados.elements[pos][1][2] = node[1][0]
                        no_visitados.change_proirity(pos, costo_nodo_actual + adjacente['peso'])
        return camino
    
    def kruskal(self, origen):
        def buscar_en_bosque(bosque, buscado):
            for index, arbol in enumerate(bosque):
                # print(buscado, arbol)
                if buscado in arbol:
                    return index

        bosque = []
        aristas = HeapMin()
        for nodo in self.elements:
            bosque.append(nodo['value'])  #agrega el nodo al bosque(cada nodo es un arbol diferente),Se crea un bosque que contiene todos los nodos como árboles separados
            adjacentes = nodo['aristas']   
            for adjacente in adjacentes:
                aristas.arrive([nodo['value'], adjacente['value']], adjacente['peso']) #agrega al heap el nodo y la arista que contiene
                                                                                    #el value que seria el nodo destino(adyacente) y el
                                                                                    #peso
        # print(aristas.elements)
        while len(bosque) > 1 and len(aristas.elements) > 0:
            # print(bosque)
            arista = aristas.atention()  #devuelve el valor eliminado del heap
            # print(arista)
            origen = buscar_en_bosque(bosque, arista[1][0])  #busca a partir del valor que se va eliminando del heap
            destino = buscar_en_bosque(bosque, arista[1][1])  #busca a partir del valor que se va eliminando del heap
            # print(origen, destino)
            if origen is not None and destino is not None:
                if origen != destino:   #chequea que ambos extremos de la arista esten en arboles diferentes(para evitar ciclos).
                    if origen > destino:
                        vertice_ori = bosque.pop(origen)  #Unir árboles: Se eliminan ambos árboles del bosque 
                        vertice_des = bosque.pop(destino) #y se combinan en uno nuevo.
                    else:
                        vertice_des = bosque.pop(destino)   
                        vertice_ori = bosque.pop(origen)
                    
                    if '-' not in vertice_ori and '-' not in vertice_des: #ambos son vértices simples
                        bosque.append(f'{vertice_ori}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_des:   #vertice_des es simple y vertice_ori es un árbol 
                        bosque.append(vertice_ori+';'+f'{arista[1][0]}-{vertice_des}-{arista[0]}')
                    elif '-' not in vertice_ori:  #vertice origen es un vertice simple y  vertice destino un arbol
                        bosque.append(vertice_des+';'+f'{vertice_ori}-{arista[1][1]}-{arista[0]}')
                    else:
                        bosque.append(vertice_ori+';'+vertice_des+';'+f'{arista[1][0]}-{arista[1][1]}-{arista[0]}')#origen y destino son un arbol
        return bosque
    


    
    



