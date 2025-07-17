# main.py
import tkinter as tk
from vista.login_vista import LoginVista

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginVista(root)
    root.mainloop()
