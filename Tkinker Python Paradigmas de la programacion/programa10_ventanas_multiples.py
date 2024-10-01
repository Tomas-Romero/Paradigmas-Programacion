# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:16:51 2023

@author: Usuario
"""

# Programa 10 - Ventanas múltiples (Toplevel)
import tkinter as tk

root = tk.Tk()
root.title("Ventana Principal")

def abrir_ventana():
    ventana_secundaria = tk.Toplevel(root) 
    ventana_secundaria.title("Ventana Secundaria")
    
    label = tk.Label(ventana_secundaria, text="Ésta es una ventana secundaria")
    label.pack()
    
boton = tk.Button(root, text="Abrir ventana", command=abrir_ventana)
boton.pack()

root.mainloop()