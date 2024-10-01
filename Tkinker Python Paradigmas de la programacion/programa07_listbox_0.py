# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:20:50 2023

@author: Usuario
"""
import tkinter as tk
root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()

listbox.insert(1, "Opción 1")
listbox.insert(2, "Opción 2") 
listbox.insert(3, "Opción 3")

label = tk.Label(root, text="Selecciona una opción")
label.pack()

def seleccionar():
  indice = listbox.curselection()[0]
  texto = listbox.get(indice)
  label.config(text=texto)
  
boton = tk.Button(root, text="Mostrar Selección", command=seleccionar)
boton.pack()
root.mainloop()