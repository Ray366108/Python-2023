import tkinter as tk
from tkinter import messagebox

## detalles de la ventana

ventana = tk.Tk()
ventana.title("Calculadora 1")
ventana.geometry("360x250")
ventana.resizable(0, 0)
ventana.iconbitmap("images.ico")

## Contornos

contorno1 = tk.LabelFrame(ventana, text = "Operaciones", font = "arial", width = 299, height = 82)
contorno1.place(x = 24, y = 30)

contorno2 = tk.LabelFrame(ventana, text = "Operadores", font = "arial", width = 299, height = 82)
contorno2.place(x = 24, y = 138)

## Operadores


def suma():
   try:
        num1 = valor1.get()
        num2 = valor2.get()
    
        if num1 == "" or num2 == "":
            messagebox.showinfo("Error", "Syntax Error")
        else:
            resultado = int(num1) + int(num2)
            result["text"] = resultado
   except:
        messagebox.showerror("Error", "Syntax Error")
        
def resta():
   
   try:
        num1 = valor1.get()
        num2 = valor2.get()
    
        if num1 == "" or num2 == "":
            messagebox.showinfo("Error", "Syntax Error")
        else:
            resultado = int(num1) - int(num2)
            result["text"] = resultado
   except:
        messagebox.showerror("Error", "Syntax Error")
        
def multi():
   
   try:
        num1 = valor1.get()
        num2 = valor2.get()
    
        if num1 == "" or num2 == "":
            messagebox.showinfo("Error", "Syntax Error")
        else:
            resultado = int(num1) * int(num2)
            result["text"] = resultado
   except:
        messagebox.showerror("Error", "Syntax Error")
        
def divi():
   
   try:
        Num_1 = valor1.get()
        Num_2 = valor2.get()
    
        if Num_1 == "" or Num_2 == "":
            messagebox.showinfo("Error", "Faltan valores")
        else:
            resultado = int(Num_1) / int(Num_2)
            result["text"] = resultado
   except:
        messagebox.showerror("Error", "Syntax Error")

##  botones de operaciones

btnsuma = tk.Button(contorno2, text = "+", font = "arial", width = 5, height = 1, command = suma)
btnsuma.place(x = 13, y = 2)

btnresta = tk.Button(contorno2, text = "-", font = "arial", width = 5, height = 1, command = resta)
btnresta.place(x = 80, y = 2)

btnmulti = tk.Button(contorno2, text = "*", font = "arial", width = 5, height = 1, command = multi)
btnmulti.place(x = 147, y = 2)

btndiv = tk.Button(contorno2, text = "/", font = "arial", width = 5, height = 1, command = divi)
btndiv.place(x = 213, y = 2)

## textbox 

valor1 = tk.Entry(contorno1, font = "arial", width = 5)
valor1.place(x = 13, y = 10)
valor1.insert(0, "0")

valor2 = tk.Entry(contorno1, font = "arial", width = 5)
valor2.place(x = 110, y = 10)
valor2.insert(0, "0")

result = tk.Label(contorno1, text = "", fg = "black", bg = "white", font=("arial", 10), width = 7)
result.place(x = 210, y = 10)

text1 = tk.Label(ventana, text = "Numero 1", font = ("arial", 10))
text1.place(x = 38, y = 100)

text2 = tk.Label(ventana, text = "Numero 2", font = ("arial", 10))
text2.place(x = 134, y = 100)

text3 = tk.Label(ventana, text = "Resultado", font = ("arial", 10))
text3.place(x = 236, y = 100)

ventana.mainloop()