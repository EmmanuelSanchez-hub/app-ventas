# modelo/producto_modelo.py
import json
import os

class Producto:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

class ProductoModelo:
    def __init__(self, archivo='datos/productos.json'):
        self.archivo = archivo

    def cargar_productos(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, 'r') as f:
            datos = json.load(f)
            return [Producto(**p) for p in datos]

    def guardar_productos(self, lista_productos):
        with open(self.archivo, 'w') as f:
            json.dump([vars(p) for p in lista_productos], f, indent=4)
