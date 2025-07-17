# controlador/cliente_controlador.py
from modelo.cliente_modelo import ClienteModelo, Cliente

class ClienteControlador:
    def __init__(self):
        self.modelo = ClienteModelo()
        self.clientes = self.modelo.cargar_clientes()
        self.ultimo_id = self._obtener_ultimo_id()

    def _obtener_ultimo_id(self):
        return max([c.id_cliente for c in self.clientes], default=0)

    def agregar_cliente(self, nombre, dni):
        self.ultimo_id += 1
        nuevo = Cliente(self.ultimo_id, nombre, dni)
        self.clientes.append(nuevo)
        self.modelo.guardar_clientes(self.clientes)

    def eliminar_cliente(self, id_cliente):
        self.clientes = [c for c in self.clientes if c.id_cliente != id_cliente]
        self.modelo.guardar_clientes(self.clientes)

    def editar_cliente(self, id_cliente, nombre, dni):
        for c in self.clientes:
            if c.id_cliente == id_cliente:
                c.nombre = nombre
                c.dni = dni
        self.modelo.guardar_clientes(self.clientes)

    def obtener_clientes(self):
        return self.clientes
