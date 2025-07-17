# controlador/usuario_controlador.py
from modelo.usuario_modelo import UsuarioModelo

class UsuarioControlador:
    def __init__(self):
        self.modelo = UsuarioModelo()

    def validar_login(self, usuario, password):
        usuarios = self.modelo.cargar_usuarios()
        for u in usuarios:
            if u.usuario == usuario and u.password == password:
                return True
        return False
