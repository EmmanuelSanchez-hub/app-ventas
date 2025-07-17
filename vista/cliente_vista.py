# vista/cliente_vista.py
import tkinter as tk
from tkinter import ttk, messagebox
from controlador.cliente_controlador import ClienteControlador

class ClienteVista:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Clientes")
        self.root.geometry("500x400")

        self.controlador = ClienteControlador()

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(self.frame, text="DNI:").grid(row=1, column=0)
        self.entry_dni = tk.Entry(self.frame)
        self.entry_dni.grid(row=1, column=1)

        self.btn_agregar = tk.Button(self.frame, text="Agregar", command=self.agregar_cliente)
        self.btn_agregar.grid(row=2, column=0, pady=5)

        self.btn_editar = tk.Button(self.frame, text="Editar", command=self.editar_cliente)
        self.btn_editar.grid(row=2, column=1)

        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "DNI"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("DNI", text="DNI")
        self.tree.pack(pady=10, fill="x")
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_fila)

        self.btn_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_cliente)
        self.btn_eliminar.pack()

        self.id_seleccionado = None
        self.refrescar_tabla()

    def agregar_cliente(self):
        nombre = self.entry_nombre.get()
        dni = self.entry_dni.get()
        if nombre and dni:
            self.controlador.agregar_cliente(nombre, dni)
            self.refrescar_tabla()
            self.entry_nombre.delete(0, tk.END)
            self.entry_dni.delete(0, tk.END)
        else:
            messagebox.showwarning("Campos incompletos", "Complete nombre y DNI.")

    def editar_cliente(self):
        if self.id_seleccionado:
            nombre = self.entry_nombre.get()
            dni = self.entry_dni.get()
            self.controlador.editar_cliente(self.id_seleccionado, nombre, dni)
            self.refrescar_tabla()
            self.entry_nombre.delete(0, tk.END)
            self.entry_dni.delete(0, tk.END)
        else:
            messagebox.showinfo("Seleccione un cliente", "Debe seleccionar un cliente primero.")

    def eliminar_cliente(self):
        if self.id_seleccionado:
            self.controlador.eliminar_cliente(self.id_seleccionado)
            self.refrescar_tabla()
            self.entry_nombre.delete(0, tk.END)
            self.entry_dni.delete(0, tk.END)
        else:
            messagebox.showinfo("Seleccione un cliente", "Debe seleccionar un cliente primero.")

    def refrescar_tabla(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)
        for c in self.controlador.obtener_clientes():
            self.tree.insert("", tk.END, values=(c.id_cliente, c.nombre, c.dni))
        self.id_seleccionado = None

    def seleccionar_fila(self, event):
        fila = self.tree.focus()
        if fila:
            valores = self.tree.item(fila, "values")
            self.id_seleccionado = int(valores[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, valores[1])
            self.entry_dni.delete(0, tk.END)
            self.entry_dni.insert(0, valores[2])
