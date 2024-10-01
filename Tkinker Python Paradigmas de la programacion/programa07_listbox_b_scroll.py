# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:02:34 2023

@author: Usuario
"""

import tkinter as tk

# Crear ventana principal 
root = tk.Tk()
root.geometry("300x200") 
# Crear un listbox vacío 
lb = tk.Listbox(root)

# Insertar opciones en el listbox
lb.insert(1, "Opcion 1")
lb.insert(2, "Opcion 2")
lb.insert(3, "Opcion 3")

# Mostrar listbox en la ventana
lb.pack()

# Iniciar el bucle de eventos 
root.mainloop()