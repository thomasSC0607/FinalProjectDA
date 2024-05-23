import random


class Estacion:  # Clase para los vertices
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.no_pasajeros = 0
        self.pasajeros_llegada = []  # El unico que implementa este atributo es la estacion Guadalajara


class Ruta:  # Clase para las aristas
    def __init__(self, estacion_inicio, estacion_destino, distancia, direccion):  # Representacion de las aristas
        self.estacion_inicio = estacion_inicio
        self.estacion_destino = estacion_destino
        self.distancia = distancia  # Peso de la arista
        self.direccion = direccion  # Direccion en grados para conocer cuando se realiza un giro

    def __str__(self):
        return f'{self.estacion_inicio.nombre} ----> {self.estacion_destino.nombre} :: distacia: {self.distancia} km'


class Ciudad:
    def __init__(self):
        self.estaciones = {}  # Diccionario de todas las estaciones
        self.caminos_lista = []  # Lista con todos los caminos
        self.rutas = []  # Lista de todas las rutas
        self.rutas_posibles_dict = {}  # Todas las rutas posibles desde A hasta B
        self.rutas_distancia_dict = {}  # Las respectivas distancias de cada ruta desde A hasta B
        self.rutas_giros_dict = {}  # Los respectivos giros realizados en cada ruta desde A hasta B
        self.total_rutas = 0  # Total de rutas posibles desde A hasta B

    def add_estacion(self, estacion):  # Agregar cada vertice a la ciudad
        self.estaciones[estacion.id] = estacion

    def add_ruta(self, estacion_inicio, estacion_destino, distancia, direccion):  # Agregar la concexion de cada vertice
        if estacion_inicio.id in self.estaciones and estacion_destino.id in self.estaciones:
            ruta = Ruta(estacion_inicio, estacion_destino, distancia, direccion)
            self.rutas.append(ruta)

    def encontrar_todas_las_rutas(self, inicio_id, destino_id, ruta_actual=None, distancia_total=0):
        if ruta_actual is None:
            ruta_actual = []  # Pasa a ser un arreglo vacio
        inicio = self.estaciones.get(inicio_id)  # Obtiene el valor de key
        destino = self.estaciones.get(destino_id)
        if inicio is None or destino is None:
            print("\nADVERTENCIA: Nodo de inicio o destino no encontrado en el grafo.")
            return
        ruta_actual = ruta_actual + [inicio]  # Agrega el nodo de inicio a la ruta actual
        if inicio == destino:
            giros_totales = self.giros(ruta_actual)
            self.mostrar_ruta(ruta_actual, distancia_total, giros_totales)
            id_ruta = self.total_rutas
            self.rutas_posibles_dict[id_ruta] = ruta_actual
            self.rutas_distancia_dict[id_ruta] = distancia_total
            self.rutas_giros_dict[id_ruta] = giros_totales
        else:
            for ruta in self.rutas:  # se itera sobre todas las rutas en la lista rutas de la ciudad.
                if ruta.estacion_inicio == inicio and ruta.estacion_destino not in ruta_actual:
                    self.encontrar_todas_las_rutas(ruta.estacion_destino.id, destino_id, ruta_actual[:],
                                                   distancia_total + ruta.distancia)

    def mostrar_ruta(self, ruta, distancia_total, giros):
        giros_totales = giros

        if ruta:
            print(f"\nRUTA {self.total_rutas} ENCONTRADA:")
            self.total_rutas += 1
            for i in range(len(ruta) - 1):
                print(f"{ruta[i].nombre} -> {ruta[i + 1].nombre}")
            print(
                f"Distancia total de la ruta: {distancia_total} km, giros totales realizados en la ruta: {giros_totales}")
            print('-' * 20)

    def mostrar_rutas_posibles(self):
        print("5 PRIMERAS RUTAS POSIBLES")
        for i, (clave, valor) in enumerate(self.rutas_posibles_dict.items()):
            if i >= 5:
                break
            print(clave, ":", valor)

    def mostrar_distancias_diccionario(self):
        print("\n5 PRIMERAS DISTANCIAS DICIONARIOS, CORRESPONDIENTES A LAS RUTAS POSIBLES\n")
        for i, (clave, valor) in enumerate(self.rutas_distancia_dict.items()):
            if i >= 5:
                break
            print(clave, ":", valor)

    # Organizar las rutas con respecto al parametro el cual es un diccionario usando MergeSort
    def organizar_rutas_distancia(self):
        items = list(self.rutas_distancia_dict.items())
        sorted_items = self.merge_sort_by_values(items)
        sorted_dict = {key: value for key, value in sorted_items}

        print("\nPRIMERAS 10 DISTANCIAS ORGANIZADAS\n")
        for i, (clave, valor) in enumerate(sorted_dict.items()):
            if i >= 10:
                break
            print('Ruta ' + str(clave), ":", str(round(valor, 3)) + ' Km')

        print("\nULTIMAS 10 DISTANCIAS ORGANIZADAS\n")
        for i, (clave, valor) in enumerate(sorted_dict.items()):
            dif = len(sorted_dict.items()) - i
            if 1 <= dif <= 10:
                print('Ruta ' + str(clave), ":", str(round(valor, 3)) + ' Km')
        sorted_keys = sorted_dict.keys()

        dic_aux = {}
        for i, clave in enumerate(sorted_keys):
            if i >= 10:
                break
            dic_aux[clave] = self.rutas_posibles_dict[clave]

        print("\nPRIMEROS 10 CAMINOS MAS RAPIDOS SEGUN KM RECORRIDOS\n")
        for clave, lista in dic_aux.items():
            nombres = '--> '.join(objeto.nombre for objeto in lista)
            print(f'Ruta {clave}: {nombres}')
            print(str(round(self.rutas_distancia_dict[clave], 3)) + ' Km\n')

        return

    def organizar_rutas_giros(self):
        items = list(self.rutas_giros_dict.items())
        sorted_items = self.merge_sort_by_values(items)
        sorted_dict = {key: value for key, value in sorted_items}

        print("\nPRIMERAS 10 DISTANCIAS ORGANIZADAS POR GIROS\n")
        for i, (clave, valor) in enumerate(sorted_dict.items()):
            if i >= 10:
                break
            print('Ruta ' + str(clave), ":", str(valor) + ' Giros')

        print("\nULTIMAS 10 DISTANCIAS ORGANIZADAS POR GIROS\n")
        for i, (clave, valor) in enumerate(sorted_dict.items()):
            dif = len(sorted_dict.items()) - i
            if 1 <= dif <= 10:
                print('Ruta ' + str(clave), ":", str(round(valor, 3)) + ' Giros')
        sorted_keys = sorted_dict.keys()

        dic_aux = {}  # Diccionario auxiliar donde se gurdan las distancias organizadas
        for i, clave in enumerate(sorted_keys):
            if i >= 10:
                break
            dic_aux[clave] = self.rutas_posibles_dict[clave]

        print("\nPRIMEROS 10 CAMINOS MAS RAPIDOS SEGUN NUMERO DE GIROS REALIZADOS\n")
        for clave, lista in dic_aux.items():
            nombres = '--> '.join(objeto.nombre for objeto in lista)
            print(f'Ruta {clave}: {nombres}')
            print(str(self.rutas_giros_dict[clave]) + ' Giros\n')

        return

    def merge_sort_by_values(self, items):
        if len(items) <= 1:
            return items

        mid = len(items) // 2
        left_half = self.merge_sort_by_values(items[:mid])
        right_half = self.merge_sort_by_values(items[mid:])

        return self.merge_by_values(left_half, right_half)

    def merge_by_values(self, left, right):
        sorted_list = []
        left_index, right_index = 0, 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index][1] <= right[right_index][1]:
                sorted_list.append(left[left_index])
                left_index += 1
            else:
                sorted_list.append(right[right_index])
                right_index += 1

        sorted_list.extend(left[left_index:])
        sorted_list.extend(right[right_index:])
        return sorted_list

    def giros(self, ruta):
        lista_rutas = []
        lista_giros = []
        giros = 0
        n = 1

        for i in range(len(ruta) - 1):
            for j in range(len(self.rutas)):
                if ruta[i] == self.rutas[j].estacion_inicio and ruta[i + 1] == self.rutas[j].estacion_destino:
                    lista_rutas.append(self.rutas[j])
                    break
        self.caminos_lista.append(lista_rutas)
        for ruta in lista_rutas:
            lista_giros.append(ruta.direccion)

        for i in range(len(lista_giros) - 1):
            if abs(lista_giros[i + 1] - lista_giros[i]) > 30:  # Un giro es un movimiento de mas de 30 grados
                giros += 1
        return giros

    def mostar_ciudad(self):
        for ruta in self.rutas:
            print(f"{ruta}")

    def buscar_ruta(self, inicio_id, destino_id):
        for ruta in self.rutas:
            if ruta.estacion_inicio.id == inicio_id and ruta.estacion_destino.id == destino_id:
                return ruta
