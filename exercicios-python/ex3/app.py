#Módulo tkinter

from tkinter import *

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
janelaPrincipal.title("Aprendendo sobre tkinter")
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

pic = PhotoImage(file="foto-p.png")
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()