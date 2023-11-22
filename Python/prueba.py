import tkinter as tk

def operacion(signo):
    
    num1 = caja1.get()
    num2 = caja2.get()
    oper = num1+signo+num2
    result.set(eval(oper))
    

root = tk.Tk()
root.geometry("700x500")

result = tk.StringVar()
result.set("0")

caja1 = tk.Entry(root)
caja1.place(x=50, y=100)

caja4 = tk.Entry(root, textvariable= operacion("signo"))
caja4.place(x=220, y=100)


caja2 = tk.Entry(root)
caja2.place(x=250, y=100)

caja3 = tk.Entry(root, textvariable= result)
caja3.place(x=450, y=100)



btnsuma = tk.Button(root, text="SUMA", command= lambda: operacion("+"))
btnsuma.place(x=50, y=150)
root.mainloop()