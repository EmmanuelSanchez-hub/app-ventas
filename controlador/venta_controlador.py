# controlador/venta_controlador.py
from modelo.venta_modelo import VentaModelo, Venta
from datetime import datetime
import numpy as np

class VentaControlador:
    def __init__(self):
        self.modelo = VentaModelo()
        self.ventas = self.modelo.cargar_ventas()
        self.ultimo_id = self._obtener_ultimo_id()

    def _obtener_ultimo_id(self):
        return max([v.id_venta for v in self.ventas], default=0)

    def registrar_venta(self, cliente, productos):
        self.ultimo_id += 1
        total = sum(p['subtotal'] for p in productos)
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        venta = Venta(self.ultimo_id, cliente, productos, total, fecha)
        self.ventas.append(venta)
        self.modelo.guardar_ventas(self.ventas)

    def obtener_ventas(self):
        return self.ventas

@staticmethod
def estadisticas_ventas(ventas):
    if not ventas:
        return {
            "total_ventas": 0,
            "monto_total": 0.0,
            "promedio": 0.0,
            "maximo": 0.0,
            "minimo": 0.0
        }

    totales = np.array([v.total for v in ventas])
    return {
        "total_ventas": len(totales),
        "monto_total": totales.sum(),
        "promedio": totales.mean(),
        "maximo": totales.max(),
        "minimo": totales.min()
    }