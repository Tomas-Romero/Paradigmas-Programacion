# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:19:58 2023

@author: Usuario
"""

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Menú con Messagebox")

menubar = tk.Menu(root)
root.config(menu=menubar)

menu = tk.Menu(menubar)

# Se agregan directamente los comandos al menú
menu.add_command(label="Mostrar Info", command=lambda: messagebox.showinfo("Info", "Mensaje informativo"))
menu.add_command(label="Mostrar Advertencia", command=lambda: messagebox.showwarning("Advertencia", "Mensaje de advertencia")) 
menu.add_command(label="Mostrar Error", command=lambda: messagebox.showerror("Error", "Mensaje de error"))

menubar.add_cascade(label="Menu", menu=menu)

root.mainloop()