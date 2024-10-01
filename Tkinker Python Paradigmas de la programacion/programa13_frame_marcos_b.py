# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:59:37 2023

@author: Usuario
"""

import tkinter as tk

root = tk.Tk()

# Frame con borde   
frame1 = tk.Frame(root, borderwidth=2, relief=tk.SUNKEN)
frame1.pack(padx=10, pady=10)

tk.Label(frame1, text="Sección 1").pack()
tk.Button(frame1, text="Botón 1").pack()  

# Otro frame con estilo diferente
frame2 = tk.Frame(root, bg="gray", width=200, height=100)
frame2.pack(pady=10)

tk.Label(frame2, text="Sección 2").place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()