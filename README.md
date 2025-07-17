# 🛒 Sistema de Ventas - Aplicación con Interfaz Gráfica en Python

Este proyecto es una aplicación de escritorio desarrollada en Python con `tkinter`, orientada a la gestión de ventas de productos. Incluye interfaz gráfica, manejo de clientes, productos, ventas, reportes y autenticación de usuarios.

## 🖥️ Tecnologías utilizadas

- Python 3.10+
- Tkinter (GUI nativa de Python)
- Pillow (para manejo de imágenes)
- NumPy (estadísticas)
- Estructura MVC (Modelo - Vista - Controlador)
- Archivos JSON para persistencia de datos

## 📦 Módulos principales

| Módulo     | Funcionalidad                                      |
|------------|-----------------------------------------------------|
| **Login**  | Inicio de sesión con validación de usuario          |
| **Clientes** | Registro, edición y listado de clientes           |
| **Productos** | Gestión de inventario de productos               |
| **Ventas** | Registro de ventas con cálculo de totales y detalle|
| **Reportes** | Visualización y exportación de ventas             |
| **Dashboard** | Estadísticas en tiempo real                      |

## 📁 Estructura del proyecto

app-ventas/
├── controlador/
├── modelo/
├── vista/
│ ├── images/
│ └── *.py
├── datos/
│ ├── productos.json
│ ├── clientes.json
│ ├── ventas.json
│ └── usuarios.json
├── main.py
