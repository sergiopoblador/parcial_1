from tkinter import *

ventana=Tk()
ventana.geometry("300x400+100+100")

lblTextEntrada=Label(text="Digite los 2 numeros que quiere graficar", font=("Arial",14)).place(x=10,y=10)
entradaTextEntrada=StringVar()


lblCedula=Label(text="x:",font=("Arial",14)).place(x=10,y=240)
entradaCedula=StringVar()
txtCedula=Entry(ventana,textvariable=entradaCedula).place(x=30,y=240)

lblNombre=Label(text="y:",font=("Arial",14)).place(x=10,y=280)
entradaNombre=StringVar()
txtNombre=Entry(ventana,textvariable=entradaNombre).place(x=30,y=280)


lblCedula=Label(text="-x:",font=("Arial",14)).place(x=10,y=320)
entradaCedula=StringVar()
txtCedula=Entry(ventana,textvariable=entradaCedula).place(x=30,y=320)

lblNombre=Label(text="-y:",font=("Arial",14)).place(x=10,y=360)
entradaNombre=StringVar()
txtNombre=Entry(ventana,textvariable=entradaNombre).place(x=30,y=360)