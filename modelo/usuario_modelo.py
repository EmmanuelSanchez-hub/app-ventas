# modelo/usuario_modelo.py
import json
import os

class Usuario:
    def __init__(self, usuario, password):
        self.usuario = usuario
        self.password = password

class UsuarioModelo:
    def __init__(self, archivo='datos/usuarios.json'):
        self.archivo = archivo

    def cargar_usuarios(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, 'r') as f:
            datos = json.load(f)
            return [Usuario(u['usuario'], u['password']) for u in datos]
