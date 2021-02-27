from os import system
from tkinter import *
from random import randint
import string

root = Tk()

def encrypt():
    def getfintext(texto):
        abecedario = string.printable + "áéíóúÁÉÍÚÓàèìòùÀÈÌÒÙäëïöüÄËÏÖÜñÑ´"
        abecedario2 = []
        nummoves = randint(1, 26)
        indexs = []

        texttoenc = []

        for l in range(0, len(abecedario)):
            abecedario2.append(abecedario[l])

        for let in range(0, len(texto.get())):
            texttoenc.append(texto.get()[let])

        for letter in texto.get():
            indexs.append(abecedario2.index(letter))

        for move in range(0, nummoves):
            abecedario2 += abecedario2.pop(0)

        texto = []

        for i in range(0, len(indexs)):
            texto.append(abecedario2[indexs[i]])
            texto.append(".")

        fintext = ""

        for letter2 in range(0, len(texto), 2):
            fintext += texto[letter2]

        fintext = str(nummoves) + "." + fintext

        final = Label(root, text="Texto encriptado: " + fintext, bg="black", fg="white")
        final.pack()

    but1.destroy()
    lab1.destroy()
    but2.destroy()

    global lab

    lab = Label(root, text="Introduzca el texto a encriptar : ", bg="black", fg="white")
    lab.pack(fill=X)

    entry = Entry(root)
    entry.pack()

    execute = Button(root, text="Encriptar", command=lambda: getfintext(entry))
    execute.pack(fill=X)

def decrypt():

    texto = input("Introduzca el texto a desencriptar : ").split(".")
    abecedario = string.printable + "áéíóúÁÉÍÚÓàèìòùÀÈÌÒÙäëïöüÄËÏÖÜñÑ´"
    abecedario2 = []
    nummoves = int(texto[0])
    indexs = []
    finalindexs = []
    textode1 = texto[1]
    textode2 = []

    for l in range(0, len(abecedario)):
        abecedario2.append(abecedario[l])

    for letter in range(0, len(textode1)):
        textode2.append(textode1[letter])

    for index in range(0, len(textode1)):
        indexs.append(abecedario.index(textode1[index]))

    for move in range(nummoves, 0):
        abecedario2 += abecedario2.pop(27)

    for value in indexs:
        newval = value - nummoves
        finalindexs.append(newval)

    textofin = ""

    for i in range(0, len(finalindexs)):
        textofin += abecedario2[finalindexs[i]]

    print(textofin)

global lab1
global but1
global but2

lab1 = Label(root, text="Encriptación de texto", bg="black", fg="white")
lab1.pack(fill=X)

but1 = Button(root, text="Encriptar", command=encrypt)
but2 = Button(root, text="Desencriptar", command=decrypt)

but1.pack(fill=X)
but2.pack(fill=X)

root.mainloop()
