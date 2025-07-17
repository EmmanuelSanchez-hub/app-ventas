# modelo/cliente_modelo.py
import json
import os

class Cliente:
    def __init__(self, id_cliente, nombre, dni):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.dni = dni

class ClienteModelo:
    def __init__(self, archivo='datos/clientes.json'):
        self.archivo = archivo

    def cargar_clientes(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, 'r') as f:
            datos = json.load(f)
            return [Cliente(**d) for d in datos]

    def guardar_clientes(self, lista_clientes):
        with open(self.archivo, 'w') as f:
            json.dump([vars(c) for c in lista_clientes], f, indent=4)
