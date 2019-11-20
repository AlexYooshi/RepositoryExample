from tkinter import *
from random import shuffle
window = Tk()
window.geometry('300x200')

def boton1():
    verbo1 = verbo.get()
    pasado(verbo1)
    
def pasado(verbo1):
    lista = []
    lista.append("Tu: "+verbo1+"ás")
    lista.append("Yo: "+verbo1+"é")
    lista.append("El: "+verbo1+"a")
    lista.append("Nosotros: "+verbo1+"émos")
    lista.append("Ustedes: "+verbo1+"án")
    lista.append("Ellos: "+verbo1+"án")
    shuffle(lista)
    mostrar(lista)
     
def mostrar(lista):
    n = len(lista)
    for i in range(0,n):
        lista1.insert(i,lista[i])

label1 = Label(window, text="Verbo en presente: ", )
label1.grid(column=0, row=0)
verbo = Entry(window, width=30)
verbo.grid(column=1, row=0)
label2 = Label(window, text="Verbo en pasado: ", )
label2.grid(column=0, row=15)
lista1 = Listbox(window, width=30)
lista1.grid(column=1, row=15)
boton = Button(window, text="Conjugar", bg="gray", fg="black", command=boton1)
boton.grid(column=1, row=10)
window.mainloop()