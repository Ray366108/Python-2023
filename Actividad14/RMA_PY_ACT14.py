import tkinter as tk
import math

ventana = tk.Tk()

## window
ventana.title("Calculadora ")
ventana.geometry("360x420")
ventana.resizable(0, 0)
ventana.iconbitmap("meme.ico")

def vlent(tecla):
    try:
        if tecla >= "0" and tecla <= "9" or tecla == ".":
            entrada.set(entrada.get() + tecla)
            
        if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
            if tecla == "*":
                entrada.set(entrada.get() + "*")

            elif tecla == "/":
                entrada.set(entrada.get() + "/")

            elif tecla == "+":
                entrada.set(entrada.get() + "+")

            elif tecla == "-":
                entrada.set(entrada.get() + "-")

    except:
        entrada.set("ERROR")

def viewresult(tecla, *args):
    try:
        resultado = eval(entrada.get())
        entrada.set(resultado)

    except:
        entrada.set("ERROR")

def raizcu():
    try:
        resultado = math.sqrt(float(entrada.get()))
        entrada.set(resultado)

    except:
        entrada.set("ERROR")

def delete(*args):
    inicio = 0
    final = len(entrada.get())
    entrada.set(entrada.get()[inicio:final-1])

def cborrar(*args):
    entrada.set("")

def mas_():
    try:
        resultado = eval(entrada.get()) + float(entrada.get())
        entrada.set(resultado)

    except:
        entrada.set("ERROR")

def mc():
    entrada.set("")

def ms():
    try:
        resultado = eval(entrada.get())
        entrada.set(resultado)

    except:
        entrada.set("ERROR")

entrada = tk.StringVar()
cajatxt = tk.Entry(ventana, font = ("Arial", 25), justify = tk.RIGHT, textvariable = entrada, bd=2)
cajatxt.place(x = 20, y = 20, width = 315, height = 27)


btnsuma = tk.Button(ventana, text = "+", command = lambda: vlent("+"))
btnsuma.place(x = 219, y = 326, width = 50, height = 50)

btnresta = tk.Button(ventana, text = "-", command = lambda: vlent("-"))
btnresta.place(x = 219, y = 260, width = 50, height = 50)

btnmult = tk.Button(ventana, text = "*", command = lambda: vlent("*"))
btnmult.place(x = 219, y = 194, width = 50, height = 50)

btndiv = tk.Button(ventana, text = "/", command = lambda: vlent("/"))
btndiv.place(x = 219, y = 128, width = 50, height = 50)

btnsqr = tk.Button(ventana, text = "sqr", command = lambda: raizcu())
btnsqr.place(x = 285, y = 62, width = 50, height = 50)

btnpunto = tk.Button(ventana, text = ".", command = lambda: vlent("."))
btnpunto.place(x = 153, y = 326, width = 50, height = 50)

btnigual = tk.Button(ventana, text = "=", command = lambda: viewresult("="))
btnigual.place(x = 285, y = 260, width = 50, height = 116)

btnmc = tk.Button(ventana, text = "MC", command = lambda: mc())
btnmc.place(x = 22, y = 62, width = 50, height = 50)

btnmr = tk.Button(ventana, text="MR", command=lambda: ms())
btnmr.place(x = 88, y = 62, width = 50, height = 50)

btnms = tk.Button(ventana, text = "MS", command = lambda: ms())
btnms.place(x = 154, y = 62, width = 50, height = 50)

btnmas = tk.Button(ventana, text = "M+", command = lambda: mas_())
btnmas.place(x = 220, y = 62, width = 50, height = 50)

btndel = tk.Button(ventana, text = "<-", command = lambda: delete())
btndel.place(x = 285, y = 194, width = 50, height = 50)

btnc = tk.Button(ventana, text = "C", command = lambda: cborrar())
btnc.place(x = 285, y = 128, width = 50, height = 50)


btn1 = tk.Button(ventana, text = "1", command = lambda: vlent("1"))
btn1.place(x = 21, y = 260, width = 50, height = 50)

btn2 = tk.Button(ventana, text = "2", command = lambda: vlent("2"))
btn2.place(x = 87, y = 260, width = 50, height = 50)

btn3 = tk.Button(ventana, text = "3", command = lambda: vlent("3"))
btn3.place(x = 153, y = 260, width = 50, height = 50)

btn4 = tk.Button(ventana, text = "4", command = lambda: vlent("4"))
btn4.place(x = 21, y = 194, width = 50, height = 50)

btn5 = tk.Button(ventana, text = "5", command = lambda: vlent("5"))
btn5.place(x = 87, y = 194, width = 50, height = 50)

btn6 = tk.Button(ventana, text = "6", command = lambda: vlent("6"))
btn6.place(x = 153, y = 194, width = 50, height = 50)

btn7 = tk.Button(ventana, text = "7", command = lambda: vlent("7"))
btn7.place(x = 21, y = 128, width = 50, height = 50)

btn8 = tk.Button(ventana, text = "8", command = lambda: vlent("8"))
btn8.place(x = 87, y = 128, width = 50, height = 50)

btn9 = tk.Button(ventana, text = "9", command = lambda: vlent("9"))
btn9.place(x = 153, y = 128, width = 50, height = 50)

btn0 = tk.Button(ventana, text = "0", command = lambda: vlent("0"))
btn0.place(x = 21, y = 326, width = 116, height = 50)

ventana.mainloop()