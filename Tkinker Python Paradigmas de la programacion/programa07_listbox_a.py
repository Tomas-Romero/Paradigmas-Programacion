# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:14:42 2023

@author: Usuario
"""
import tkinter as tk
root = tk.Tk()

listbox = tk.Listbox(root) ## defino un listbox
listbox.pack() ## lo empaqueto y lo muestro en la ventana root

for i in range(10):
    listbox.insert(tk.END, f"Opción {i}")  ### cargo el listbox con opciones

label = tk.Label(root, text="Selecciona una opción") 
label.pack()

def seleccionar():
    indice = listbox.curselection()[0]
    texto = listbox.get(indice)
    label.config(text=texto)

boton = tk.Button(root, text="Mostrar Selección", command=seleccionar)
boton.pack()

root.mainloop()