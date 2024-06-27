def registrarLibro(registro,titulo,autor,genero,precio):
    for libro in registro:
        if libro['titulo'].lower() == titulo.lower():
            print("Libro registrado correctamente!")
            return
    dicLibro = {
        'titulo' : titulo ,
        'autor' : autor ,
        'género' : genero ,
        'precio' : precio
    }
    registro.append(dicLibro)

def listarLibros(registro):
    for libro in registro:
        print(libro)

def registrarVenta(registroVent,tituloLib,cantVen,precioUni,precioFinal):
    for libro in registroVent:
        if libro['titulo'].lower() == tituloLib.lower():
            print("Ventas registradas correctamente!")
            return
    dicVentas = {
        'Titulo Libro' : tituloLib ,
        'Cantidad Vendida' : cantVen ,
        'Precio Unidad' : precioUni ,
        'Precio Final' : precioFinal
    }
    registroVent.append(dicVentas)

def imprimirReporte(registro,cateLibro,genero):
    encontrado = False
    for libro in registro:
        if libro['género'].lower() == genero.lower():
            print("El libro pertenece al género: ",genero)
            encontrado = True
            return
    categoriaLibro = {
        'Acción' : genero ,
        'No Ficción' : genero ,
        'Ciencia Ficcion' : genero
    }
    registro.append(cateLibro)


    

def generarTxt(registroVent,nombreArchivo):
    with open(nombreArchivo,'w') as archivo:
        for libro in registroVent:
            archivo.write(f"Titulo del Libro: {libro['Titulo Libro']} Cantidad Vendida: {libro['Cantidad Vendida']} Precio Unidad: {libro['Precio Unidad']} Precio Final: {libro['Precio Final']}")
 

