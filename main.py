from tkinter import *

# from calculadora import soma

# import calculadora

janela = Tk()
janela.title('Calculadora')

texto_orientacao = Label(
    janela, text="Calculadora desenvolvida para estudos em Python")

texto_orientacao.grid(column=0, row=0)

botao1 = Button(janela, text="Soma")
botao1.grid(column=1, row=1, padx=100, pady=200)
janela.mainloop()
