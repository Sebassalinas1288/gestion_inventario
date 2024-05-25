from repositorio import RepositorioInventario
from servicios import ServicioInventario

def mostrar_menu():
    print("Sistema de Gestión de Inventario")
    print("1. Registrar Categoría")
    print("2. Registrar Producto")
    print("3. Registrar Proveedor")
    print("4. Registrar Bodega")
    print("5. Salir")

def registrar_categoria(servicio):
    nombre = input("Ingrese el nombre de la categoría: ")
    descripcion = input("Ingrese la descripción de la categoría: ")
    categoria = servicio.registrar_categoria(nombre, descripcion)
    print(f"Categoría '{categoria.nombre}' registrada con éxito.")

def registrar_producto(servicio):
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock_inicial = int(input("Ingrese el stock inicial del producto: "))
    categoria_nombre = input("Ingrese el nombre de la categoría del producto: ")
    
    # Buscar la categoría en el repositorio
    categoria = next((c for c in servicio.repositorio.categorias if c.nombre == categoria_nombre), None)
    if categoria:
        producto = servicio.registrar_producto(nombre, descripcion, precio, stock_inicial, categoria)
        print(f"Producto '{producto.nombre}' registrado con éxito.")
    else:
        print(f"Categoría '{categoria_nombre}' no encontrada.")

def registrar_proveedor(servicio):
    nombre = input("Ingrese el nombre del proveedor: ")
    direccion = input("Ingrese la dirección del proveedor: ")
    telefono = input("Ingrese el teléfono del proveedor: ")
    proveedor = servicio.registrar_proveedor(nombre, direccion, telefono)
    print(f"Proveedor '{proveedor.nombre}' registrado con éxito.")

def registrar_bodega(servicio):
    nombre = input("Ingrese el nombre de la bodega: ")
    ubicacion = input("Ingrese la ubicación de la bodega: ")
    capacidad_maxima = int(input("Ingrese la capacidad máxima de la bodega: "))
    bodega = servicio.registrar_bodega(nombre, ubicacion, capacidad_maxima)
    print(f"Bodega '{bodega.nombre}' registrada con éxito.")

def main():
    repositorio = RepositorioInventario()
    servicio = ServicioInventario(repositorio)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_categoria(servicio)
        elif opcion == "2":
            registrar_producto(servicio)
        elif opcion == "3":
            registrar_proveedor(servicio)
        elif opcion == "4":
            registrar_bodega(servicio)
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

def mostrar_menu():
    print("Sistema de Gestión de Inventario")
    print("1. Registrar Categoría")
    print("2. Registrar Producto")
    print("3. Registrar Proveedor")
    print("4. Registrar Bodega")
    print("5. Agregar Stock")
    print("6. Retirar Stock")
    print("7. Consultar Producto")
    print("8. Salir")

def agregar_stock(servicio):
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad a agregar: "))
    servicio.agregar_stock(nombre_producto, cantidad)

def retirar_stock(servicio):
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad a retirar: "))
    servicio.retirar_stock(nombre_producto, cantidad)

def consultar_producto(servicio):
    nombre_producto = input("Ingrese el nombre del producto: ")
    servicio.consultar_producto(nombre_producto)

def main():
    repositorio = RepositorioInventario()
    servicio = ServicioInventario(repositorio)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_categoria(servicio)
        elif opcion == "2":
            registrar_producto(servicio)
        elif opcion == "3":
            registrar_proveedor(servicio)
        elif opcion == "4":
            registrar_bodega(servicio)
        elif opcion == "5":
            agregar_stock(servicio)
        elif opcion == "6":
            retirar_stock(servicio)
        elif opcion == "7":
            consultar_producto(servicio)
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    main()
