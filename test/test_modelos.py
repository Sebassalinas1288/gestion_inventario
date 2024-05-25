import unittest
from gestion_inventario.modelos import Producto, Categoria, Proveedor, Bodega

class TestModelos(unittest.TestCase):

    def test_crear_producto(self):
        categoria = Categoria("Electrónica", "Dispositivos Electrónicos")
        producto = Producto("Laptop", "Laptop para juegos", 1500, 10, categoria)
        self.assertEqual(producto.nombre, "Laptop")
        self.assertEqual(producto.descripcion, "Laptop para juegos")
        self.assertEqual(producto.precio, 1500)
        self.assertEqual(producto.stock, 10)
        self.assertEqual(producto.categoria, categoria)

    def test_crear_categoria(self):
        categoria = Categoria("Electrónica", "Dispositivos Electrónicos")
        self.assertEqual(categoria.nombre, "Electrónica")
        self.assertEqual(categoria.descripcion, "Dispositivos Electrónicos")
        self.assertEqual(categoria.productos, [])

    def test_crear_proveedor(self):
        proveedor = Proveedor("Proveedor Tech", "Calle Tech 123", "555-1234")
        self.assertEqual(proveedor.nombre, "Proveedor Tech")
        self.assertEqual(proveedor.direccion, "Calle Tech 123")
        self.assertEqual(proveedor.telefono, "555-1234")
        self.assertEqual(proveedor.productos_suministrados, [])

    def test_crear_bodega(self):
        bodega = Bodega("Bodega Principal", "Calle Bodega 456", 1000)
        self.assertEqual(bodega.nombre, "Bodega Principal")
        self.assertEqual(bodega.ubicacion, "Calle Bodega 456")
        self.assertEqual(bodega.capacidad_maxima, 1000)
        self.assertEqual(bodega.productos_almacenados, [])

if __name__ == '__main__':
    unittest.main()
