class RepositorioInventario:
    def __init__(self):
        self.productos = []
        self.categorias = []
        self.proveedores = []
        self.bodegas = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
    
    def agregar_categoria(self, categoria):
        self.categorias.append(categoria)
    
    def agregar_proveedor(self, proveedor):
        self.proveedores.append(proveedor)
    
    def agregar_bodega(self, bodega):
        self.bodegas.append(bodega)
    
    # Implementar otros métodos del repositorio para buscar, actualizar y eliminar entidades

