import tkinter as tk

def msge(band):
    lbl_msge = tk.Label(root, text= "hoolaaaa")
    lbl_msge.place(x= 50, y= 50)


root = tk.Tk()
root.geometry("500x350+450+100")
#boton suma
btn_suma = tk.Button(root, text= "+", command= lambda: msge(1))
btn_suma.config(width=10, height=3)
btn_suma.place(x=60, y=210)
#boton resta
btn_resta = tk.Button(root, text= "-")
btn_resta.config(width= 10, height=3)
btn_resta.place(x= 160, y= 210)
#boton multiplicacion
btn_mult = tk.Button(root, text="*")
btn_mult.config(width=10, height=3)
btn_mult.place(x=260, y=210)
#boton divicion
btn_div = tk.Button(root, text="/")
btn_div.config(width=10, height=3)
btn_div.place(x=360, y=210)




root.mainloop()