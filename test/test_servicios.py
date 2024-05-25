import unittest
from gestion_inventario.repositorio import RepositorioInventario
from gestion_inventario.servicios import ServicioInventario
from gestion_inventario.modelos import Categoria, Producto

class TestServicios(unittest.TestCase):

    def setUp(self):
        self.repositorio = RepositorioInventario()
        self.servicio = ServicioInventario(self.repositorio)

    def test_registrar_categoria(self):
        categoria = self.servicio.registrar_categoria("Electrónica", "Dispositivos Electrónicos")
        self.assertEqual(categoria.nombre, "Electrónica")
        self.assertEqual(categoria.descripcion, "Dispositivos Electrónicos")
        self.assertIn(categoria, self.repositorio.categorias)

    def test_registrar_producto(self):
        categoria = self.servicio.registrar_categoria("Electrónica", "Dispositivos Electrónicos")
        producto = self.servicio.registrar_producto("Laptop", "Laptop para juegos", 1500, 10, categoria)
        self.assertEqual(producto.nombre, "Laptop")
        self.assertEqual(producto.descripcion, "Laptop para juegos")
        self.assertEqual(producto.precio, 1500)
        self.assertEqual(producto.stock, 10)
        self.assertEqual(producto.categoria, categoria)
        self.assertIn(producto, self.repositorio.productos)

    def test_registrar_proveedor(self):
        proveedor = self.servicio.registrar_proveedor("Proveedor Tech", "Calle Tech 123", "555-1234")
        self.assertEqual(proveedor.nombre, "Proveedor Tech")
        self.assertEqual(proveedor.direccion, "Calle Tech 123")
        self.assertEqual(proveedor.telefono, "555-1234")
        self.assertIn(proveedor, self.repositorio.proveedores)

    def test_registrar_bodega(self):
        bodega = self.servicio.registrar_bodega("Bodega Principal", "Calle Bodega 456", 1000)
        self.assertEqual(bodega.nombre, "Bodega Principal")
        self.assertEqual(bodega.ubicacion, "Calle Bodega 456")
        self.assertEqual(bodega.capacidad_maxima, 1000)
        self.assertIn(bodega, self.repositorio.bodegas)

if __name__ == '__main__':
    unittest.main()
