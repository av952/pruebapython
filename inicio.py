import tkinter
import random
from tkinter import messagebox


def btn_accion():
    numero1= int(entrada.get())

    numero2= int(entrada2.get())

    resultado = numero1+numero2

    resultado= str(resultado)

    #entrada.delete(0, "end")
    #entrada2.delete(0,"end")
    respuestasuma.delete(0,"end")

    #random.randrange([start,] stop [,step]) , random.randrange(stop)
    ran = random.randrange(numero1,numero2,1)

    respuestasuma.insert("a",ran)

    # print("hola soy el boton 1")
    #messagebox.showinfo("suma", "mi boton ha sido precionado"+resultado)


def btn_emergente():
    messagebox.showinfo("info", "boton emergente")
    pregunta = messagebox.askyesno("pregunta", "queires saber como te llmas?")

    if pregunta:
        messagebox.showinfo("nombre", "te llamas " + entrada.get())
    else:
        print("dijo no")


ventana = tkinter.Tk()

ventana.title("Azar")
ventana.geometry("200x100")

# para crear el boton
boton = tkinter.Button(text="Random", command=btn_accion)
boton2 = tkinter.Button(text="click2", command=btn_accion)
boton3 = tkinter.Button(text="emergente", command=btn_emergente)
# para colocarlo en ventana
# entradas
entrada = tkinter.Entry()
entrada2= tkinter.Entry()
respuestasuma= tkinter.Entry()

entrada.pack()
entrada2.pack()
respuestasuma.pack()
boton.pack()
#boton2.pack()
#boton3.pack()

ventana.mainloop()
