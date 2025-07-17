# vista/venta_vista.py
import tkinter as tk
from tkinter import ttk, messagebox
from controlador.venta_controlador import VentaControlador
from controlador.cliente_controlador import ClienteControlador
from controlador.producto_controlador import ProductoControlador

class VentaVista:
    def __init__(self, root):
        self.root = root
        self.root.title("Registrar Venta")
        self.root.geometry("600x500")

        self.venta_controlador = VentaControlador()
        self.cliente_controlador = ClienteControlador()
        self.producto_controlador = ProductoControlador()

        self.detalle_venta = []

        # Cliente
        tk.Label(root, text="Cliente:").pack()
        self.combo_cliente = ttk.Combobox(root, state="readonly")
        self.combo_cliente['values'] = [f"{c.id_cliente} - {c.nombre}" for c in self.cliente_controlador.obtener_clientes()]
        self.combo_cliente.pack(pady=5)

        # Producto y cantidad
        frame = tk.Frame(root)
        frame.pack(pady=5)

        tk.Label(frame, text="Producto:").grid(row=0, column=0)
        self.combo_producto = ttk.Combobox(frame, state="readonly")
        self.combo_producto['values'] = [f"{p.id_producto} - {p.nombre}" for p in self.producto_controlador.obtener_productos()]
        self.combo_producto.grid(row=0, column=1)

        tk.Label(frame, text="Cantidad:").grid(row=0, column=2)
        self.entry_cantidad = tk.Entry(frame, width=5)
        self.entry_cantidad.grid(row=0, column=3)

        tk.Button(frame, text="Agregar", command=self.agregar_producto).grid(row=0, column=4, padx=10)

        # Detalle
        self.tree = ttk.Treeview(root, columns=("Producto", "Cantidad", "PU", "Subtotal"), show="headings")
        for col in ("Producto", "Cantidad", "PU", "Subtotal"):
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="x")

        # Total
        self.label_total = tk.Label(root, text="Total: S/. 0.00", font=('Arial', 12, 'bold'))
        self.label_total.pack(pady=5)

        # Guardar venta
        tk.Button(root, text="Registrar Venta", command=self.registrar_venta).pack(pady=10)

    def agregar_producto(self):
        producto_str = self.combo_producto.get()
        cantidad_str = self.entry_cantidad.get()

        if not producto_str or not cantidad_str:
            messagebox.showwarning("Faltan datos", "Seleccione un producto y cantidad")
            return

        try:
            cantidad = int(cantidad_str)
            if cantidad <= 0:
                raise ValueError

            id_prod = int(producto_str.split(" - ")[0])
            producto = next(p for p in self.producto_controlador.obtener_productos() if p.id_producto == id_prod)

            subtotal = producto.precio * cantidad
            self.detalle_venta.append({
                'nombre': producto.nombre,
                'cantidad': cantidad,
                'precio_unitario': producto.precio,
                'subtotal': subtotal
            })

            self.tree.insert("", tk.END, values=(producto.nombre, cantidad, f"S/. {producto.precio:.2f}", f"S/. {subtotal:.2f}"))
            self.actualizar_total()
            self.entry_cantidad.delete(0, tk.END)

        except ValueError:
            messagebox.showerror("Error", "Cantidad inválida")

    def actualizar_total(self):
        total = sum(p['subtotal'] for p in self.detalle_venta)
        self.label_total.config(text=f"Total: S/. {total:.2f}")

    def registrar_venta(self):
        cliente_str = self.combo_cliente.get()
        if not cliente_str or not self.detalle_venta:
            messagebox.showwarning("Faltan datos", "Seleccione cliente y agregue productos")
            return

        cliente = cliente_str.split(" - ")[1]
        self.venta_controlador.registrar_venta(cliente, self.detalle_venta)
        messagebox.showinfo("Éxito", "Venta registrada correctamente")
        self.tree.delete(*self.tree.get_children())
        self.detalle_venta = []
        self.actualizar_total()

