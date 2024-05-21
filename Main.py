from Estaciones import *

if __name__ == "__main__":
    ciudad = Ciudad()

    VE1 = Estacion('V1', 'VE1')
    VE2 = Estacion('V2', 'VE2')
    VE3 = Estacion('V3', 'VE3')
    VE4 = Estacion('V4', 'VE4')
    VE5 = Estacion('V5', 'VE5')
    VE6 = Estacion('V6', 'VE6')
    VE7 = Estacion('V7', 'VE7')
    VE8 = Estacion('V8', 'VE8')
    VE9 = Estacion('V9', 'VE9')
    VE10 = Estacion('V10', 'VE10')
    VE11 = Estacion('V11', 'VE11')
    VE12 = Estacion('V12', 'VE12')
    VE13 = Estacion('V13', 'VE13')
    VE14 = Estacion('V14', 'VE14')
    VE15 = Estacion('V15', 'VE15')
    VE16 = Estacion('V16', 'VE16')
    VE17 = Estacion('V17', 'VE17')
    VE18 = Estacion('V18', 'VE18')
    VE19 = Estacion('V19', 'VE19')
    VE20 = Estacion('V20', 'VE20')
    VE21 = Estacion('V21', 'VE21')
    VE22 = Estacion('V22', 'VE22')
    VE23 = Estacion('V23', 'VE23')
    VE24 = Estacion('V24', 'VE24')
    VE25 = Estacion('V25', 'VE25')
    VE26 = Estacion('V26', 'VE26')
    VE27 = Estacion('V27', 'VE27')
    VE28 = Estacion('V28', 'VE28')
    VE29 = Estacion('V29', 'VE29')
    VE30 = Estacion('V30', 'VE30')
    VE31 = Estacion('V31', 'VE31')
    VE32 = Estacion('V32', 'VE32')
    VE33 = Estacion('V33', 'VE33')
    VE34 = Estacion('V34', 'VE34')
    VE35 = Estacion('V35', 'VE35')
    VE36 = Estacion('V36', 'VE36')
    VE37 = Estacion('V37', 'VE37')
    VE38 = Estacion('V38', 'VE38')
    VE39 = Estacion('V39', 'VE39')
    VE40 = Estacion('V40', 'VE40')
    VE41 = Estacion('V41', 'VE41')
    VE42 = Estacion('V42', 'VE42')
    VE43 = Estacion('V43', 'VE43')
    VE44 = Estacion('V44', 'VE44')

    ciudad.add_estacion(VE1)
    ciudad.add_estacion(VE3)
    ciudad.add_estacion(VE4)
    ciudad.add_estacion(VE5)
    ciudad.add_estacion(VE6)
    ciudad.add_estacion(VE7)
    ciudad.add_estacion(VE8)
    ciudad.add_estacion(VE9)
    ciudad.add_estacion(VE10)
    ciudad.add_estacion(VE11)
    ciudad.add_estacion(VE12)
    ciudad.add_estacion(VE13)
    ciudad.add_estacion(VE14)
    ciudad.add_estacion(VE15)
    ciudad.add_estacion(VE16)
    ciudad.add_estacion(VE17)
    ciudad.add_estacion(VE18)
    ciudad.add_estacion(VE19)
    ciudad.add_estacion(VE20)
    ciudad.add_estacion(VE21)
    ciudad.add_estacion(VE22)
    ciudad.add_estacion(VE23)
    ciudad.add_estacion(VE24)
    ciudad.add_estacion(VE25)
    ciudad.add_estacion(VE26)
    ciudad.add_estacion(VE27)
    ciudad.add_estacion(VE28)
    ciudad.add_estacion(VE29)
    ciudad.add_estacion(VE30)
    ciudad.add_estacion(VE31)
    ciudad.add_estacion(VE32)
    ciudad.add_estacion(VE33)
    ciudad.add_estacion(VE34)
    ciudad.add_estacion(VE35)
    ciudad.add_estacion(VE36)
    ciudad.add_estacion(VE37)
    ciudad.add_estacion(VE38)
    ciudad.add_estacion(VE39)
    ciudad.add_estacion(VE40)
    ciudad.add_estacion(VE41)
    ciudad.add_estacion(VE42)
    ciudad.add_estacion(VE43)
    ciudad.add_estacion(VE44)

    ciudad.add_ruta(VE1, VE4, 0.071, 320)
    ciudad.add_ruta(VE4, VE8, 0.057, 320)
    ciudad.add_ruta(VE8, VE11, 0.090, 320)
    ciudad.add_ruta(VE11, VE13, 0.080, 320)
    ciudad.add_ruta(VE13, VE17, 0.079, 320)
    ciudad.add_ruta(VE17, VE34, 0.184, 320)
    ciudad.add_ruta(VE34, VE39, 0.175, 320)
    ciudad.add_ruta(VE39, VE42, 0.246, 320)
    ciudad.add_ruta(VE42, VE41, 0.072, 165)

    ciudad.add_ruta(VE41, VE40, 0.070, 180)
    ciudad.add_ruta(VE40, VE41, 0.070, 0)

    ciudad.add_ruta(VE40, VE36, 0.099, 180)
    ciudad.add_ruta(VE36, VE40, 0.099, 0)

    ciudad.add_ruta(VE36, VE35, 0.079, 180)
    ciudad.add_ruta(VE35, VE36, 0.079, 0)

    ciudad.add_ruta(VE35, VE29, 0.081, 180)
    ciudad.add_ruta(VE29, VE35, 0.079, 0)

    ciudad.add_ruta(VE29, VE26, 0.186, 180)
    ciudad.add_ruta(VE26, VE29, 0.186, 0)

    ciudad.add_ruta(VE26, VE25, 0.076, 180)
    ciudad.add_ruta(VE25, VE26, 0.076, 0)

    ciudad.add_ruta(VE25, VE24, 0.119, 90)

    ciudad.add_ruta(VE24, VE26, 0.155, 315)

    ciudad.add_ruta(VE26, VE18, 0.020, 120)
    ciudad.add_ruta(VE18, VE26, 0.020, 300)

    ciudad.add_ruta(VE18, VE16, 0.097, 90)
    ciudad.add_ruta(VE16, VE18, 0.097, 270)

    ciudad.add_ruta(VE16, VE12, 0.097, 90)
    ciudad.add_ruta(VE12, VE16, 0.097, 270)

    ciudad.add_ruta(VE12, VE9, 0.079, 90)
    ciudad.add_ruta(VE9, VE12, 0.079, 270)

    ciudad.add_ruta(VE9, VE6, 0.070, 90)
    ciudad.add_ruta(VE6, VE9, 0.070, 270)

    ciudad.add_ruta(VE6, VE3, 0.119, 90)
    ciudad.add_ruta(VE3, VE6, 0.119, 270)

    ciudad.add_ruta(VE3, VE5, 0.067, 345)
    ciudad.add_ruta(VE5, VE2, 0.052, 125)
    ciudad.add_ruta(VE3, VE2, 0.030, 45)

    ciudad.add_ruta(VE2, VE1, 0.100, 45)
    ciudad.add_ruta(VE1, VE2, 0.100, 225)

    ciudad.add_ruta(VE5, VE4, 0.099, 45)
    ciudad.add_ruta(VE4, VE5, 0.099, 225)

    ciudad.add_ruta(VE5, VE7, 0.061, 190)
    ciudad.add_ruta(VE7, VE5, 0.100, 110)

    ciudad.add_ruta(VE8, VE7, 0.103, 220)

    ciudad.add_ruta(VE7, VE6, 0.121, 220)
    ciudad.add_ruta(VE7, VE10, 0.098, 305)

    ciudad.add_ruta(VE9, VE43, 0.067, 8)

    ciudad.add_ruta(VE43, VE10, 0.116, 25)
    ciudad.add_ruta(VE10, VE11, 0.102, 40)

    ciudad.add_ruta(VE43, VE15, 0.105, 310)
    ciudad.add_ruta(VE15, VE43, 0.105, 130)

    ciudad.add_ruta(VE12, VE15, 0.124, 0)

    ciudad.add_ruta(VE16, VE15, 0.135, 40)
    ciudad.add_ruta(VE15, VE16, 0.135, 220)

    ciudad.add_ruta(VE15, VE14, 0.108, 40)
    ciudad.add_ruta(VE14, VE15, 0.108, 220)

    ciudad.add_ruta(VE10, VE14, 0.077, 310)
    ciudad.add_ruta(VE14, VE10, 0.077, 130)

    ciudad.add_ruta(VE14, VE13, 0.105, 40)
    ciudad.add_ruta(VE13, VE14, 0.105, 220)

    ciudad.add_ruta(VE15, VE22, 0.085, 340)
    ciudad.add_ruta(VE22, VE15, 0.085, 160)

    ciudad.add_ruta(VE14, VE23, 0.077, 305)
    ciudad.add_ruta(VE23, VE14, 0.077, 125)

    ciudad.add_ruta(VE17, VE44, 0.062, 220)
    ciudad.add_ruta(VE44, VE23, 0.050, 220)
    ciudad.add_ruta(VE23, VE22, 0.073, 220)
    ciudad.add_ruta(VE22, VE21, 0.064, 220)
    ciudad.add_ruta(VE21, VE20, 0.069, 220)
    ciudad.add_ruta(VE20, VE19, 0.065, 220)
    ciudad.add_ruta(VE19, VE18, 0.051, 220)

    ciudad.add_ruta(VE44, VE33, 0.178, 310)
    ciudad.add_ruta(VE33, VE44, 0.178, 130)

    ciudad.add_ruta(VE23, VE32, 0.180, 305)

    ciudad.add_ruta(VE22, VE31, 0.180, 305)
    ciudad.add_ruta(VE31, VE22, 0.180, 130)

    ciudad.add_ruta(VE21, VE30, 0.180, 305)
    ciudad.add_ruta(VE30, VE21, 0.180, 130)

    ciudad.add_ruta(VE20, VE27, 0.180, 305)
    ciudad.add_ruta(VE27, VE20, 0.180, 130)

    ciudad.add_ruta(VE19, VE28, 0.180, 305)
    ciudad.add_ruta(VE28, VE19, 0.180, 130)

    ciudad.add_ruta(VE28, VE27, 0.68, 40)
    ciudad.add_ruta(VE27, VE28, 0.68, 220)

    ciudad.add_ruta(VE27, VE30, 0.65, 40)
    ciudad.add_ruta(VE30, VE27, 0.65, 220)

    ciudad.add_ruta(VE30, VE31, 0.65, 40)
    ciudad.add_ruta(VE31, VE30, 0.65, 220)

    ciudad.add_ruta(VE31, VE32, 0.65, 40)
    ciudad.add_ruta(VE32, VE31, 0.65, 220)

    ciudad.add_ruta(VE32, VE33, 0.65, 40)
    ciudad.add_ruta(VE33, VE32, 0.65, 220)
    ciudad.add_ruta(VE33, VE34, 0.80, 40)

    ciudad.add_ruta(VE27, VE29, 0.79, 305)
    ciudad.add_ruta(VE29, VE27, 0.79, 125)

    ciudad.add_ruta(VE30, VE35, 0.131, 305)
    ciudad.add_ruta(VE35, VE30, 0.131, 125)

    ciudad.add_ruta(VE31, VE36, 0.175, 305)
    ciudad.add_ruta(VE36, VE31, 0.175, 125)

    ciudad.add_ruta(VE32, VE37, 0.175, 305)
    ciudad.add_ruta(VE37, VE32, 0.175, 125)

    ciudad.add_ruta(VE33, VE38, 0.175, 305)
    ciudad.add_ruta(VE38, VE33, 0.175, 125)

    ciudad.add_ruta(VE37, VE36, 0.069, 220)
    ciudad.add_ruta(VE36, VE37, 0.069, 40)

    ciudad.add_ruta(VE37, VE38, 0.058, 40)
    ciudad.add_ruta(VE38, VE37, 0.058, 220)

    ciudad.add_ruta(VE38, VE39, 0.054, 40)
    ciudad.add_ruta(VE39, VE38, 0.054, 220)

    ciudad.add_ruta(VE37, VE40, 0.068, 305)
    ciudad.add_ruta(VE40, VE37, 0.068, 125)

    ciudad.add_ruta(VE38, VE41, 0.115, 305)
    ciudad.add_ruta(VE41, VE38, 0.115, 125)

    def menu():
        print("\nBienvenido al programa, ENCONTRAR RUTAS DESDE MCDONALD'S HASTA PERGAMINO CAFÉ")
        opciones = int(input("\nSeleccione la opción a proseguir:\n"
                             "1. Mostar todas las rutas posibles\n"
                             "2. Organizar e imprimir las rutas con respecto a la menor distancia recorrida\n"
                             "3. Organizar e imprimir las rutas con respecto a la menor cantidad de giros realizados\n"
                             "4. Finalizar programa\n\n"))

        while opciones < 1 or opciones > 4:
            opciones = int(input("\nSeleccione una opción correcta Dios mio, entre 1 y 4, no entre menos infinito e "
                                 "infinito:\n"
                                 "1. Mostar todas las rutas posibles\n"
                                 "2. Organizar e imprimir las rutas con respecto a la menor distancia recorrida\n"
                                 "3. Organizar e imprimir las rutas con respecto a la menor cantidad de giros "
                                 "realizados\n"
                                 "4. Finalizar programa\n"))

        if opciones == 1:
            ciudad.mostar_ciudad()
            # Encuentra todas las rutas desde mc al cafe
            print("\nTODAS LAS RUTAS POSIBLES DESDE MCDONALD'S HASTA CAFÉ PERGAMINO\n")
            ciudad.encontrar_todas_las_rutas('V8', 'V20')
            print(f"Rutas posibles totales: {ciudad.total_rutas}")
            menu()
        if opciones == 2:
            print("\nRUTAS ORGANIZADAS CON RESPECTO A LA DISTANCIA RECORRIDA EN KM\n")
            ciudad.organizar_rutas(ciudad.rutas_distancia_dict)
            menu()
        if opciones == 3:
            print("\nRUTAS ORGANIZADAS CON RESPECTO A LA MENOR CANTIDAD DE GIROS REALIZADOS\n")
            ciudad.organizar_rutas(ciudad.rutas_giros_dict)
            menu()
        if opciones == 4:
            print("\nGRACIAS POR USAR NUESTRO PROGRAMA\n")

    menu()
