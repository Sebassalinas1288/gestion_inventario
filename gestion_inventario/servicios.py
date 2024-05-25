from modelos import Producto, Categoria, Proveedor, Bodega

class ServicioInventario:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def registrar_producto(self, nombre, descripcion, precio, stock_inicial, categoria):
        producto = Producto(nombre, descripcion, precio, stock_inicial, categoria)
        self.repositorio.agregar_producto(producto)
        return producto

    def registrar_categoria(self, nombre, descripcion):
        categoria = Categoria(nombre, descripcion)
        self.repositorio.agregar_categoria(categoria)
        return categoria

    def registrar_proveedor(self, nombre, direccion, telefono):
        proveedor = Proveedor(nombre, direccion, telefono)
        self.repositorio.agregar_proveedor(proveedor)
        return proveedor

    def registrar_bodega(self, nombre, ubicacion, capacidad_maxima):
        bodega = Bodega(nombre, ubicacion, capacidad_maxima)
        self.repositorio.ag

    def agregar_stock(self, nombre_producto, cantidad):
        producto = next((p for p in self.repositorio.productos if p.nombre == nombre_producto), None)
        if producto:
            producto.stock += cantidad
            print(f"Se han agregado {cantidad} unidades al stock de '{producto.nombre}'.")
        else:
            print(f"Producto '{nombre_producto}' no encontrado.")

    def retirar_stock(self, nombre_producto, cantidad):
        producto = next((p for p in self.repositorio.productos if p.nombre == nombre_producto), None)
        if producto:
            if producto.stock >= cantidad:
                producto.stock -= cantidad
                print(f"Se han retirado {cantidad} unidades del stock de '{producto.nombre}'.")
            else:
                print(f"No hay suficiente stock de '{producto.nombre}'.")
        else:
            print(f"Producto '{nombre_producto}' no encontrado.")

    def consultar_producto(self, nombre_producto):
        producto = next((p for p in self.repositorio.productos if p.nombre == nombre_producto), None)
        if producto:
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Precio: {producto.precio}")
            print(f"Stock: {producto.stock}")
            print(f"Categoría: {producto.categoria.nombre}")
        else:
            print(f"Producto '{nombre_producto}' no encontrado.")
