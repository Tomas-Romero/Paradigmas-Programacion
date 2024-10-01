# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:15:48 2023

@author: Usuario
"""

# Programa 9 - Ventanas emergentes (Message Box)
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Ventanas Emergentes")

def mostrar_info():
   messagebox.showinfo("Información", "Mensaje informativo")
   
def mostrar_advertencia():
   messagebox.showwarning("Advertencia", "Mensaje de advertencia")  

def mostrar_error():
   messagebox.showerror("Error", "Mensaje de error")
   
tk.Button(root, text="Mostrar Info", command=mostrar_info).pack()
tk.Button(root, text="Mostrar Advertencia", command=mostrar_advertencia).pack()
tk.Button(root, text="Mostrar Error", command=mostrar_error).pack()

root.mainloop()