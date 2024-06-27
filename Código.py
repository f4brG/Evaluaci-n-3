import funcionesCod as fn

regLibros = []
regVentas = []
cateLibro = ['Ciencia Ficción','No ficción','Acción']

while True:
    print("---Menú---")
    print("1. Registrar Libro")
    print("2. Listar todos los libros")
    print("3. Registrar Venta")
    print("4. Imprir reporte de ventas")
    print("5. Generar txt")
    print("6. Salir")
    try:
        opc = int(input("Seleccione opción: "))

        if opc ==1:
            titulo = input("Ingrese titulo del libro: ")
            autor = input("Ingrese autor del libro: ")
            genero = input("Ingrese género del libro: ")
            precio = int(input("Ingrese precio del libro: "))
            fn.registrarLibro(regLibros,titulo,autor,genero,precio)
            print()
            print("Libro registrado correctamente!")
            print()


        elif opc ==2:
            fn.listarLibros(regLibros)

        elif opc ==3:
            tituloLibro = input("Ingrese título del libro: ")
            cantidadVen = int(input("Ingrese cantidad vendida: "))
            precioUnidad = int(input("Ingrese precio por unidad: "))
            precioFinal = int(input("Ingrese precio final: "))

            fn.registrarVenta(regVentas,tituloLibro,cantidadVen,precioUnidad,precioFinal)

        elif opc ==4:
            print("1. Imprimir Todos")
            print("2. Imprimir por Género")
            opcImp = int(input("Seleccione una opción: "))
            if opcImp ==1:
                print(regLibros)
            elif opcImp ==2:
                print("A. Acción")
                print("B. No Ficción")
                print("C. Ciencia Ficción")
                opcGen = input("Seleccione Género: ").lower()
                print(fn.imprimirReporte(regLibros,cateLibro,genero))

        elif opc ==5:
            nombreArhivo = "Registro Ventas.txt"
            fn.generarTxt(regVentas,nombreArhivo)
            print("Transferencia de archivo a .txt exitosamente!")

        elif opc ==6:
            break
        else:
            print("¡Opción Inválida!")
    except:
        print("¡¡Acción no válida!!")