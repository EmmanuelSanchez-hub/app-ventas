# modelo/venta_modelo.py
import json
import os
from datetime import datetime

class Venta:
    def __init__(self, id_venta, cliente, productos, total, fecha):
        self.id_venta = id_venta
        self.cliente = cliente
        self.productos = productos  # lista de dicts: [{nombre, cantidad, precio_unitario, subtotal}]
        self.total = total
        self.fecha = fecha

class VentaModelo:
    def __init__(self, archivo='datos/ventas.json'):
        self.archivo = archivo

    def cargar_ventas(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, 'r') as f:
            datos = json.load(f)
            return [Venta(**v) for v in datos]

    def guardar_ventas(self, lista_ventas):
        with open(self.archivo, 'w') as f:
            json.dump([vars(v) for v in lista_ventas], f, indent=4)
