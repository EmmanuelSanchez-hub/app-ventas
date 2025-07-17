# vista/reporte_vista.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from controlador.venta_controlador import VentaControlador
import csv

class ReporteVista:
    def __init__(self, root):
        self.root = root
        self.root.title("Reporte de Ventas")
        self.root.geometry("700x400")

        self.controlador = VentaControlador()
        self.ventas = self.controlador.obtener_ventas()

        tk.Label(root, text="Ventas Registradas", font=('Arial', 14)).pack(pady=10)

        # Tabla
        self.tree = ttk.Treeview(root, columns=("ID", "Cliente", "Fecha", "Total"), show="headings")
        for col in ("ID", "Cliente", "Fecha", "Total"):
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="x")

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Ver Detalle", command=self.ver_detalle).pack(side="left", padx=5)
        tk.Button(btn_frame, text="Exportar a CSV", command=self.exportar_csv).pack(side="left", padx=5)

        self.cargar_tabla()

    def cargar_tabla(self):
        for fila in self.tree.get_children():
            self.tree.delete(fila)
        for v in self.ventas:
            self.tree.insert("", tk.END, values=(v.id_venta, v.cliente, v.fecha, f"S/. {v.total:.2f}"))

    def ver_detalle(self):
        seleccionado = self.tree.focus()
        if not seleccionado:
            messagebox.showwarning("Selecciona una venta", "Debes seleccionar una venta.")
            return
        datos = self.tree.item(seleccionado)['values']
        id_venta = int(datos[0])
        venta = next((v for v in self.ventas if v.id_venta == id_venta), None)

        if venta:
            detalle = "\n".join([
                f"{p['nombre']} x{p['cantidad']} = S/. {p['subtotal']:.2f}"
                for p in venta.productos
            ])
            messagebox.showinfo("Detalle de venta", f"Cliente: {venta.cliente}\nFecha: {venta.fecha}\n\n{detalle}\n\nTotal: S/. {venta.total:.2f}")

    def exportar_csv(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if not archivo:
            return
        try:
            with open(archivo, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["ID", "Cliente", "Fecha", "Total"])
                for v in self.ventas:
                    writer.writerow([v.id_venta, v.cliente, v.fecha, v.total])
            messagebox.showinfo("Éxito", f"Reporte exportado como {archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {e}")
