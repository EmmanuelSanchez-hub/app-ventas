# controlador/producto_controlador.py
from modelo.producto_modelo import ProductoModelo, Producto

class ProductoControlador:
    def __init__(self):
        self.modelo = ProductoModelo()
        self.productos = self.modelo.cargar_productos()
        self.ultimo_id = self._obtener_ultimo_id()

    def _obtener_ultimo_id(self):
        return max((p.id_producto for p in self.productos), default=0)

    def agregar_producto(self, nombre, precio, stock):
        self.ultimo_id += 1
        nuevo = Producto(self.ultimo_id, nombre, precio, stock)
        self.productos.append(nuevo)
        self.modelo.guardar_productos(self.productos)

    def editar_producto(self, id_producto, nombre, precio, stock):
        for p in self.productos:
            if p.id_producto == id_producto:
                p.nombre = nombre
                p.precio = precio
                p.stock = stock
        self.modelo.guardar_productos(self.productos)

    def eliminar_producto(self, id_producto):
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        self.modelo.guardar_productos(self.productos)

    def obtener_productos(self):
        return self.productos
