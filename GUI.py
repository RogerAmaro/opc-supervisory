#confing: utf-8

from Tkinter import *
from random import randint
janela = Tk()
import OpenOPC
from time import sleep,time

sensor = []
contP = 0
start = time()

def timer():
    newtime = time()
    tempo =  newtime - start
    
    

def contagem():
    global contP
    global sensor
    if read("Operando")=="True":
        if read("Sensor_opticoD")=="True":
            if sensor[-1]!="True":
                sensor.append(1)
        else:
            if sensor[-1]!="False":
                sensor.append(0)
    return sensor




def estado():
    tags = [["Parado",read("Parado")],["Parando",read("Parando")],["Manoal",read("Manoal")],["Reiniciando",read("Reiniciando")],["Pronto",read("Pronto")],["Operando",read("Operando")]]

    for i in tags:
       if i[1]=="True":
          return i[0]

 

def connect(name = "OPC.SimaticHMI.CoRtHmiRTm"):
    objOpc = OpenOPC.client()
    objOpc.connect(name)
    return objOpc

def set_var(tag):
    connect().write((tag,1))
    sleep(0.1)
    connect().write((tag,0))


def read(tag):
    return str(connect()[tag])


def bt_start():
    set_var("Botao_Start_Remoto")
    def reset_color():
        bt_start.configure(bg="gainsboro")
    bt_start.configure(bg = "green")
    janela.after(100,reset_color)

def bt_stop():
    set_var("Botao_Stop_Remoto")
    def reset_color():
        bt_stop.configure(bg="gainsboro")
    bt_stop.configure(bg = "red")
    janela.after(100,reset_color)
def bt_reset():
    set_var("Botao_Reset_Remoto")


bt_start = Button(janela, width=10, text="START", command=bt_start)
bt_start.place(x=100,y=20)

bt_stop = Button(janela, width=10, text="STOP", command=bt_stop)
bt_stop.place(x=300,y=20)

bt_reset = Button(janela, width=10, text="RESET", command=bt_reset)
bt_reset.place(x=500,y=20)



label_operando = Label(janela, text="STATUS:", background="gray")
label_operando.place(x=700,y=20)

label_section = Label(janela,text="_________________________________________________________________________________________________________________________________________________________", background="gray")
label_section.place(x=10, y=60)

label_producao = Label(janela, text="PRODUCAO:", background="gray")
label_producao.place(x=10,y=90)

label_tempo = Label(janela, text="TIMER:", background="gray")
label_tempo.place(x=10,y=130)

label_qtdpes = Label(janela, text="QTD PECAS:", background="gray")
label_qtdpes.place(x=10,y=170)

label_pressao = Label(janela, text="PRESSAO:", background="gray")
label_pressao.place(x=10,y=210)
#------------------------------------------------------------#

state_system = "OPERANDO"
text_operando =  Label(janela, text="", background="gray")
text_operando.place(x=760,y=20)
#------------------------------------------------------------#
def setV():
    text_producao.configure(text= contagem())
    text_timeProd.configure(text=timer())
    text_operando.configure(text = estado())
    return janela.after(100,setV)
    


text_producao = Label(janela,text="----", background="gray")
text_producao.place(x=100,y=90)


text_timeProd = Label(janela,text="------", background="gray")
text_timeProd.place(x=100,y=130)

text_timeProd = Label(janela,text="------", background="gray")
text_timeProd.place(x=100,y=170)

text_press =  Label(janela,text="------", background="gray")
text_press.place(x=100,y=210)

text_operando = Label(janela, text="--", background="gray")
text_operando.place(x=750,y=20)

#buttons(janela)
#textsLabels(janela)









janela.geometry("900x500")
janela['bg']="gray"
janela.title("SISTEMA SUPERVISORIO MUSCLE FLUID PRESS")


print(contagem())



setV()
#janela.mainloop()







