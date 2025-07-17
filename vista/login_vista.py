# vista/login_vista.py
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from controlador.usuario_controlador import UsuarioControlador
from vista.menu_principal import MenuPrincipal
import os

class LoginVista:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        self.root.geometry("650x300")
        self.root.configure(bg="#e9f0f7")

        self.controlador = UsuarioControlador()

        # Contenedor horizontal principal
        contenedor = tk.Frame(root, bg="#e9f0f7")
        contenedor.pack(expand=True, fill="both", padx=20, pady=20)

        # FORMULARIO a la IZQUIERDA
        form_frame = tk.Frame(contenedor, bg="#e9f0f7")
        form_frame.pack(side="left", padx=20, fill="y")

        tk.Label(form_frame, text="INICIO DE SESIÓN", font=("Helvetica", 16, "bold"),
                 bg="#e9f0f7", fg="#1e3c72").pack(pady=(0, 20))

        tk.Label(form_frame, text="Usuario:", font=("Helvetica", 11), bg="#e9f0f7").pack(anchor="w")
        self.entry_usuario = tk.Entry(form_frame, font=("Helvetica", 11), width=30)
        self.entry_usuario.pack(pady=5)

        tk.Label(form_frame, text="Contraseña:", font=("Helvetica", 11), bg="#e9f0f7").pack(anchor="w")
        self.entry_password = tk.Entry(form_frame, font=("Helvetica", 11), width=30, show="*")
        self.entry_password.pack(pady=5)

        tk.Button(form_frame, text="Iniciar sesión", font=("Helvetica", 11, "bold"),
                  bg="#007acc", fg="white", activebackground="#005f99",
                  width=20, bd=0, relief="flat", cursor="hand2",
                  command=self.validar_login).pack(pady=20)

        # IMAGEN a la DERECHA
        imagen_frame = tk.Frame(contenedor, bg="#e9f0f7")
        imagen_frame.pack(side="left", padx=20)

        ruta_imagen = "vista/images/login.png"
        try:
            imagen = Image.open(ruta_imagen)
            imagen = imagen.resize((320, 320), Image.LANCZOS)
            self.img_tk = ImageTk.PhotoImage(imagen)
            tk.Label(imagen_frame, image=self.img_tk, bg="#e9f0f7").pack(expand=True)
        except Exception as e:
            print("ERROR AL CARGAR IMAGEN:", e)
            tk.Label(imagen_frame, text="[Imagen no encontrada]", font=("Helvetica", 10),
                     bg="#e9f0f7", fg="red").pack()

    def validar_login(self):
        usuario = self.entry_usuario.get()
        password = self.entry_password.get()

        if self.controlador.validar_login(usuario, password):
            self.root.destroy()
            nueva_ventana = tk.Tk()
            MenuPrincipal(nueva_ventana)
            nueva_ventana.mainloop()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
