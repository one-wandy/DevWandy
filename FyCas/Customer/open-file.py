import tkinter as tk
from tkinter import messagebox
import os
import subprocess
import platform

def open_or_create_folder():
    try:
        folder_path = os.path.join(os.path.expanduser("~"), "Olivares", "Doc")
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        if platform.system() == "Windows":
            subprocess.Popen(f'explorer {folder_path}')
        elif platform.system() == "Linux":
            subprocess.Popen(['xdg-open', folder_path])
        else:
            messagebox.showerror("Error", "Sistema operativo no soportado.")
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal

# Abrir o crear la carpeta especificada al iniciar el programa
open_or_create_folder()

# Salir del programa
root.quit()
