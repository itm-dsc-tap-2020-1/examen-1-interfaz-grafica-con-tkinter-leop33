import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
def respuestas():
    a=r1.get()
    b=r2.get()
    c=opcion.get()
    d=opcion2.get()
    e=opcion_1.get()
    f=opcion_2.get()
    g=opcion_3.get()
    x1=0
    x2=0
    x3=0
    x4=0
    x5=0
    x6=0
    x7=0
    if a=="portugues":x1=20
    if b=="Oceania":x2=20
    if c==2:x3=20
    if d==1:x4=20
    if e==1 and f==1 and g==0 :x5=20
    r=x1+x2+x3+x4+x5+x6+x7
    mBox.showinfo(message=("TU CALIFICAION ES",r),title="Respuestas")
ventana=tk.Tk()    
ventana.title("Examen")
ttk.Label(ventana, text="Examen de Geografia").grid(column=0,row=0)
ttk.Label(ventana, text="Que idioma hablan en brazil").grid(column=0,row=1)
r1=tk.StringVar()
r1C=ttk.Entry(ventana, width=12, textvariable=r1)
r1C.grid(column=1,row=1)
ttk.Label(ventana, text="Continente que comienza con '0'").grid(column=0,row=2)
r2=tk.StringVar()
r2C=ttk.Entry(ventana, width=12, textvariable=r2)
r2C.grid(column=1,row=2)
ttk.Label(ventana, text="Numero de Continentes").grid(column=0,row=3)
opcion=tk.IntVar()
radio1=tk.Radiobutton(ventana,text="4",variable=opcion,value=1)
radio1.grid(column=0,row=4,sticky=tk.W)
radio2=tk.Radiobutton(ventana,text="5",variable=opcion,value=2)
radio2.grid(column=1,row=4,sticky=tk.W)
radio3=tk.Radiobutton(ventana,text="7",variable=opcion,value=3)
radio3.grid(column=2,row=4,sticky=tk.W)
ttk.Label(ventana, text="Estados de la republica mexicana").grid(column=0,row=5)
opcion2=tk.IntVar()
radio4=tk.Radiobutton(ventana,text="32",variable=opcion2,value=1)
radio4.grid(column=0,row=6,sticky=tk.W)
radio5=tk.Radiobutton(ventana,text="30",variable=opcion2,value=2)
radio5.grid(column=1,row=6,sticky=tk.W)
radio6=tk.Radiobutton(ventana,text="31",variable=opcion2,value=3)
radio6.grid(column=2,row=6,sticky=tk.W)
ttk.Label(ventana, text="Paises en America").grid(column=0,row=7)
opcion_1=tk.IntVar()
casilla_1=tk.Checkbutton(ventana, text="Mexico", variable=opcion_1)
casilla_1.grid(column=0,row=8,sticky=tk.W)
opcion_2=tk.IntVar()
casilla_2=tk.Checkbutton(ventana, text="Colombia", variable=opcion_2)
casilla_2.grid(column=1,row=8,sticky=tk.W)
opcion_3=tk.IntVar()
casilla_3=tk.Checkbutton(ventana, text="España", variable=opcion_3)
casilla_3.grid(column=2,row=8,sticky=tk.W)
accion=ttk.Button(ventana,text="Resultado",command=respuestas)
accion.grid(column=3,row=9)
ventana.mainloop()