# vista/menu_principal.py
import tkinter as tk
from vista.cliente_vista import ClienteVista
from vista.producto_vista import ProductoVista
from vista.venta_vista import VentaVista
from vista.reporte_vista import ReporteVista
from controlador.venta_controlador import VentaControlador, estadisticas_ventas

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")
        self.root.geometry("700x400")
        self.root.configure(bg="#f0f0f0")

        # Título superior
        tk.Label(root, text="SISTEMA DE VENTAS", font=("Helvetica", 18, "bold"),
                 fg="#1e3c72", bg="#f0f0f0").pack(pady=10)

        # Contenedor principal con dos columnas
        contenedor = tk.Frame(root, bg="#f0f0f0")
        contenedor.pack(fill="both", expand=True, padx=20, pady=10)

        # FRAME IZQUIERDO - BOTONES
        botones_frame = tk.Frame(contenedor, bg="#f0f0f0")
        botones_frame.pack(side="left", padx=40, pady=10)

        estilo_boton = {
            "font": ("Helvetica", 12),
            "bg": "#007acc",
            "fg": "white",
            "activebackground": "#005f99",
            "activeforeground": "white",
            "width": 20,
            "height": 2,
            "bd": 0,
            "relief": "flat",
            "cursor": "hand2"
        }

        tk.Button(botones_frame, text="Clientes", command=self.abrir_clientes, **estilo_boton).pack(pady=5)
        tk.Button(botones_frame, text="Productos", command=self.abrir_productos, **estilo_boton).pack(pady=5)
        tk.Button(botones_frame, text="Ventas", command=self.abrir_ventas, **estilo_boton).pack(pady=5)
        tk.Button(botones_frame, text="Reportes", command=self.abrir_reportes, **estilo_boton).pack(pady=5)

        # FRAME DERECHO - ESTADÍSTICAS
        stats_frame = tk.Frame(contenedor, bg="#eaf4fb", bd=2, relief="groove")
        stats_frame.pack(side="left", padx=20, pady=10, fill="y")

        tk.Label(stats_frame, text="📊 Estadísticas de Ventas", font=("Helvetica", 13, "bold"),
                 fg="#004c99", bg="#eaf4fb").pack(pady=(10, 15))

        self.venta_controlador = VentaControlador()
        stats = estadisticas_ventas(self.venta_controlador.obtener_ventas())

        linea_estilo = {
            "font": ("Helvetica", 11),
            "bg": "#eaf4fb",
            "anchor": "w",
            "justify": "left",
            "width": 40,
            "padx": 10,
            "pady": 2
        }

        tk.Label(stats_frame, text=f"🧾 Total de ventas: {stats['total_ventas']}", fg="#003366", **linea_estilo).pack()
        tk.Label(stats_frame, text=f"💰 Monto total vendido: S/. {stats['monto_total']:.2f}", fg="#006699", **linea_estilo).pack()
        tk.Label(stats_frame, text=f"📈 Promedio por venta: S/. {stats['promedio']:.2f}", fg="#006633", **linea_estilo).pack()
        tk.Label(stats_frame, text=f"🔺 Máximo: S/. {stats['maximo']:.2f}", fg="#990000", **linea_estilo).pack()
        tk.Label(stats_frame, text=f"🔻 Mínimo: S/. {stats['minimo']:.2f}", fg="#cc6600", **linea_estilo).pack()

        # Pie de página
        tk.Label(root, text="© 2025 Tu Empresa", font=("Helvetica", 9),
                 fg="#666666", bg="#f0f0f0").pack(side="bottom", pady=10)

    # FUNCIONES PARA ABRIR MÓDULOS
    def abrir_clientes(self):
        ventana = tk.Toplevel(self.root)
        ClienteVista(ventana)

    def abrir_productos(self):
        ventana = tk.Toplevel(self.root)
        ProductoVista(ventana)

    def abrir_ventas(self):
        ventana = tk.Toplevel(self.root)
        VentaVista(ventana)

    def abrir_reportes(self):
        ventana = tk.Toplevel(self.root)
        ReporteVista(ventana)
