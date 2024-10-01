# -*- coding: utf-8 -*-
""" """
import tkinter as tk

def mostrar_seleccion():
    seleccion = listbox.curselection()  ## obtiene los elementos seleccionados actualmente en un widget listbox
    if seleccion:
        indice = seleccion[0]  ## Obtiene primer índice de selección
        texto_seleccionado = listbox.get(indice)  ## Obtiene texto del elemento seleccionado según su índice.
        etiqueta.config(text="Elem. selec.: " + texto_seleccionado)
    else:
        etiqueta.config(text="No seleccionado")

root = tk.Tk()
root.title("Listbox y Scrollbar")

listbox = tk.Listbox(root)
listbox.pack()

scrollbar = tk.Scrollbar(root) ## Crea barra de desplazamiento y la empaqueta.
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)  ##Sincroniza scrollbar y listbox.
## Configura el listbox para que envíe su evento yscrollcommand a la función .set() de la scrollbar.
## yscrollcommand se dispara cuando el listbox se desplaza verticalmente.
## .set() ajusta la posición de la barra de desplazamiento en la scrollbar.

## side=tk.RIGHT posiciona el widget a la derecha.
## fill=tk.BOTH hace que el widget se expanda para llenar espacio extra en ambos ejes cuando la ventana se redimensiona

for i in range(50):
    listbox.insert(tk.END, f"Elemento {i}")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
## Configura la scrollbar para que su evento command llame al método .yview() del listbox.
## command se dispara cuando se mueve la barra de desplazamiento.
## .yview() desplaza el contenido del listbox verticalmente.

boton_mostrar = tk.Button(root, text="Mostrar Selección", command=mostrar_seleccion)
boton_mostrar.pack()

etiqueta = tk.Label(root, text="Ningún elemento seleccionado")
etiqueta.pack()

root.mainloop()
