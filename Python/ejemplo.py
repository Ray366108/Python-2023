import tkinter as tk
from tkinter import ttk

def mostrar_gif():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Mostrar GIF en Tkinter")

    # Cargar el archivo GIF
    gif_path = "gato.gif"  # Reemplaza con la ruta de tu archivo GIF
    gif_image = tk.PhotoImage(file=gif_path)

    # Crear un Label para mostrar el GIF
    gif_label = ttk.Label(root, image=gif_image)
    gif_label.pack(padx=10, pady=10)
    btn_suma = tk.Button(root, text= "+", command= lambda: msge(1))
    btn_suma.config(width=10, height=3)
    btn_suma.place(x=60, y=210)
    #boton resta
    btn_resta = tk.Button(root, text= "-")
    btn_resta.config(width= 10, height=3)
    btn_resta.place(x= 160, y= 210)


    # Iniciar el bucle principal
    root.mainloop()

# Llamar a la función para mostrar el GIF
mostrar_gif()
