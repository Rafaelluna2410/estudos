from tkinter import *
import instalador_anydesk as ts

janela = Tk()
janela.title("Lojas")
janela.geometry('300x200')
janela.resizable(False, False)

label_loja_A = Label(janela, width=10, height=2, text='Loja A:', font=('Arial 15'))
label_loja_A.grid(row=0, column=0)
bota_A = Button(janela, width=14, height=1, text='selecionar loja A', bg='White', command=ts.test_event)
bota_A.grid(row=0, column=1)



label_loja_B = Label(janela, width=10, height=2, text='Loja B:', font=('Arial 15'))
label_loja_B.grid(row=1, column=0)
bota_B = Button(janela, width=14, height=1, text='selecionar loja B', bg='White', command=ts.test_event)
bota_B.grid(row=1, column=1)

label_loja_C = Label(janela, width=10, height=2, text='Loja C:', font=('Arial 15'))
label_loja_C.grid(row=2, column=0)
bota_C = Button(janela, width=14, height=1, text='selecionar loja C', bg='White', command=ts.test_event)
bota_C.grid(row=2, column=1)

janela.mainloop()