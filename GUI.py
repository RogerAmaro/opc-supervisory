from Tkinter import *
from random import randint
janela = Tk()


def buttons(janela):

    def bt_start():
        def reset_color():
            bt_start.configure(bg="gainsboro")
        bt_start.configure(bg = "green")
        janela.after(2000,reset_color)

    def bt_stop():
        def reset_color():
            bt_stop.configure(bg="gainsboro")
        bt_stop.configure(bg = "red")
        janela.after(2000,reset_color)
    def bt_reset():
        lb["text"]="O botão reset foi pressionado"


    bt_start = Button(janela, width=10, text="START", command=bt_start)
    bt_start.place(x=100,y=20)

    bt_stop = Button(janela, width=10, text="STOP", command=bt_stop)
    bt_stop.place(x=300,y=20)

    bt_reset = Button(janela, width=10, text="RESET", command=bt_reset)
    bt_reset.place(x=500,y=20)

def teste():
    return str(randint(0,100))



def imagem():
    imagem = PhotoImage(file="/home/roger/Documentos/GUI_supervisório/logo.png")
    w = Label(janela, image=imagem)
    w.imagem = imagem
    w.place(x=800,y=365)



def textsLabels(janela):
    label_operando = Label(janela, text="STATUS:", background="gray")
    label_operando.place(x=700,y=20)

    label_section = Label(janela,text="_____________________________________________________________________________________________________________________________", background="gray")
    label_section.place(x=10, y=60)

    label_producao = Label(janela, text="PRODUÇÃO:", background="gray")
    label_producao.place(x=10,y=90)

    label_tempo = Label(janela, text="TIMER:", background="gray")
    label_tempo.place(x=10,y=130)

    label_qtdpeçs = Label(janela, text="QTD PEÇAS:", background="gray")
    label_qtdpeçs.place(x=10,y=170)

    label_pressao = Label(janela, text="PRESSÃO:", background="gray")
    label_pressao.place(x=10,y=210)
    #------------------------------------------------------------#

    state_system = " OPERANDO"
    text_operando =  Label(janela, text="", background="gray")
    text_operando.configure(text=teste())
    text_operando.place(x=760,y=20)
    #------------------------------------------------------------#

    text_produção = Label(janela,text="------", background="gray")
    text_produção.place(x=100,y=90)

    text_timeProd = Label(janela,text="------", background="gray")
    text_timeProd.place(x=100,y=130)

    text_timeProd = Label(janela,text="------", background="gray")
    text_timeProd.place(x=100,y=170)

    text_press =  Label(janela,text="------", background="gray")
    text_press.place(x=100,y=210)



buttons(janela)
textsLabels(janela)











janela.geometry("900x500")
janela['bg']="gray"
janela.title("SISTEMA SUPERVISÓRIO MUSCLE FLUID PRESS")







janela.mainloop()




