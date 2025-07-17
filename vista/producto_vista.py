# vista/producto_vista.py
import tkinter as tk
from tkinter import ttk, messagebox
from controlador.producto_controlador import ProductoControlador

class ProductoVista:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")
        self.root.geometry("500x450")

        self.controlador = ProductoControlador()
        self.id_seleccionado = None

        self.frame = tk.Frame(root)
        self.frame.pack(pady=10)

        tk.Label(self.frame, text="Nombre:").grid(row=0, column=0)
        self.entry_nombre = tk.Entry(self.frame)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(self.frame, text="Precio:").grid(row=1, column=0)
        self.entry_precio = tk.Entry(self.frame)
        self.entry_precio.grid(row=1, column=1)

        tk.Label(self.frame, text="Stock:").grid(row=2, column=0)
        self.entry_stock = tk.Entry(self.frame)
        self.entry_stock.grid(row=2, column=1)

        tk.Button(self.frame, text="Agregar", command=self.agregar).grid(row=3, column=0, pady=5)
        tk.Button(self.frame, text="Editar", command=self.editar).grid(row=3, column=1)

        self.tree = ttk.Treeview(root, columns=("ID", "Nombre", "Precio", "Stock"), show="headings")
        for col in ("ID", "Nombre", "Precio", "Stock"):
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="x")
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar)

        tk.Button(root, text="Eliminar", command=self.eliminar).pack()

        self.refrescar()

    def agregar(self):
        try:
            nombre = self.entry_nombre.get()
            precio = float(self.entry_precio.get())
            stock = int(self.entry_stock.get())
            if nombre:
                self.controlador.agregar_producto(nombre, precio, stock)
                self.refrescar()
                self.limpiar_campos()
            else:
                messagebox.showwarning("Campos", "Nombre requerido.")
        except ValueError:
            messagebox.showerror("Error", "Precio y stock deben ser numéricos.")

    def editar(self):
        if self.id_seleccionado is not None:
            try:
                nombre = self.entry_nombre.get()
                precio = float(self.entry_precio.get())
                stock = int(self.entry_stock.get())
                self.controlador.editar_producto(self.id_seleccionado, nombre, precio, stock)
                self.refrescar()
                self.limpiar_campos()
            except ValueError:
                messagebox.showerror("Error", "Precio y stock deben ser numéricos.")
        else:
            messagebox.showinfo("Seleccione", "Seleccione un producto para editar.")

    def eliminar(self):
        if self.id_seleccionado is not None:
            self.controlador.eliminar_producto(self.id_seleccionado)
            self.refrescar()
            self.limpiar_campos()
        else:
            messagebox.showinfo("Seleccione", "Seleccione un producto para eliminar.")

    def seleccionar(self, event):
        fila = self.tree.focus()
        if fila:
            valores = self.tree.item(fila, "values")
            self.id_seleccionado = int(valores[0])
            self.entry_nombre.delete(0, tk.END)
            self.entry_nombre.insert(0, valores[1])
            self.entry_precio.delete(0, tk.END)
            self.entry_precio.insert(0, valores[2])
            self.entry_stock.delete(0, tk.END)
            self.entry_stock.insert(0, valores[3])

    def refrescar(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)
        for p in self.controlador.obtener_productos():
            self.tree.insert("", tk.END, values=(p.id_producto, p.nombre, p.precio, p.stock))
        self.id_seleccionado = None

    def limpiar_campos(self):
        self.entry_nombre.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)
