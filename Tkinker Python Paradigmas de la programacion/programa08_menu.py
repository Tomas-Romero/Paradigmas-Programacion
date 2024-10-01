# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:14:11 2023

@author: Usuario
"""

# Programa 8 - Menú desplegable 
import tkinter as tk

root = tk.Tk()
root.title("Menú Desplegable")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
file_menu.add_command(label="Nuevo")
file_menu.add_command(label="Abrir")
file_menu.add_separator()  
file_menu.add_command(label="Salir", command=root.quit)

edit_menu = tk.Menu(menubar)
edit_menu.add_command(label="Cortar")
edit_menu.add_command(label="Copiar")
edit_menu.add_command(label="Pegar")

menubar.add_cascade(label="Archivo", menu=file_menu)
menubar.add_cascade(label="Editar", menu=edit_menu)

root.mainloop()