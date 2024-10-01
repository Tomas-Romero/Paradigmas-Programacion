# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 12:48:28 2023

@author: Usuario
"""

import tkinter as tk
root = tk.Tk() ## def ventana pricipal 

# Frame para agrupar widgets relacionados
frame1 = tk.Frame(root) 
frame1.pack()

# Widgets en frame1
tk.Label(frame1, text="Sección 1").pack()  
tk.Button(frame1, text="Botón 1").pack()

# Otro frame
frame2 = tk.Frame(root)
frame2.pack() 

# Widgets frame 2   
tk.Label(frame2, text="Sección 2").pack()
tk.Button(frame2, text="Botón 2").pack()

root.mainloop()