# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 13:01:15 2023

@author: Usuario
"""

import tkinter as tk
root = tk.Tk()

# Frame 1 - Verde
frame1 = tk.Frame(root, bg="green") 
frame1.pack(pady=10)

entry1 = tk.Entry(frame1)
entry1.pack(padx=10, pady=10)

# Frame 2 - Celeste  
frame2 = tk.Frame(root, bg="cyan")
frame2.pack(pady=10)

entry2 = tk.Entry(frame2)
entry2.pack(padx=10, pady=10)

# Botón en ventana principal 
btn = tk.Button(root, text="Botón")
btn.pack(pady=10)

root.mainloop()