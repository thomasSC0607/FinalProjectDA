import random


class Estacion:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.no_pasajeros = 0
        self.pasajeros_llegada = []  # El unico que implementa este atributo es la estacion Guadalajara


class Ruta:
    def __init__(self, estacion_inicio, estacion_destino, distancia, direccion):  # Representacion de las aristas
        self.estacion_inicio = estacion_inicio
        self.estacion_destino = estacion_destino
        self.distancia = distancia  # Peso de la arista
        self.direccion = direccion

    def __str__(self):
        return f'{self.estacion_inicio.nombre} ----> {self.estacion_destino.nombre} :: distacia: {self.distancia} km'


class Ciudad:
    def __init__(self):
        self.estaciones = {}  # Diccionario de todas las estaciones
        self.caminos_dic = {}
        self.caminos_lista = []
        self.rutas = []  # Lista de todas las rutas
        self.total_rutas = 0

    def imprimir_caminos(self):
        for clave, valor in self.caminos_dic.items():
            print(clave, ":", valor)

    def add_estacion(self, estacion):
        self.estaciones[estacion.id] = estacion

    def add_ruta(self, estacion_inicio, estacion_destino, distancia, direccion):
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
        else:
            for ruta in self.rutas:  # se itera sobre todas las rutas en la lista rutas de la ciudad.
                if ruta.estacion_inicio == inicio and ruta.estacion_destino not in ruta_actual:
                    self.encontrar_todas_las_rutas(ruta.estacion_destino.id, destino_id, ruta_actual[:],
                                                   distancia_total + ruta.distancia)

    def mostrar_ruta(self, ruta, distancia_total, giros):
        giros_totales = giros
        n = 1
        if ruta:
            print(f"\nRUTA ENCONTRADA:")
            self.total_rutas += 1
            for i in range(len(ruta) - 1):
                print(f"{ruta[i].nombre} -> {ruta[i + 1].nombre}")
            print(
                f"Distancia total de la ruta: {distancia_total} km, giros totales realizados en la ruta: {giros_totales}")
            print('-' * 20)

    def organizar_rutas_distancia(self):
        n = len(self.caminos_dic)
        for i in range(n):
            for j in range(0, n - i - 1):
                return

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
            if abs(lista_giros[i + 1] - lista_giros[i]) > 30:
                giros += 1
        return giros

    def add_caminos_dic(self):
        n = 1
        for ruta in self.caminos_lista:
            self.caminos_dic['Ruta ' + str(n)] = ruta
            n += 1

    def mostar_ciudad(self):
        for ruta in self.rutas:
            print(f"{ruta}")

    def buscar_ruta(self, inicio_id, destino_id):
        for ruta in self.rutas:
            if ruta.estacion_inicio.id == inicio_id and ruta.estacion_destino.id == destino_id:
                return ruta
