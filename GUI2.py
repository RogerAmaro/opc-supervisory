#confing: utf-8

from Tkinter import *
from random import randint
janela = Tk()
import OpenOPC
from time import sleep,time
from datetime import datetime
sensor = ["0"]
contP = 0

def timer():
    return read("I")

def contagemPython():
    global contP
    global sensor
    print(sensor)
    if read("Operando")=="True":
        if sensor==[]:
            if read("Sensor_opticoD")=="True":
                sensor.append("1")
            else:
                sensor.append("0")
        else:
            if read("Sensor_opticoD")=="True":
                if sensor[-1]=="1":
                    pass
                else:
                    sensor.append("1")
            else:
                if sensor[-1]=="0":
                    pass
                    #sensor.append("1")
                else:
                    sensor.append("0")
        if read("Desliza_DirS") =="True" and read("Atuador")=="False":
            for i in sensor:
                if i=="1":
                    contP=contP+1
            sensor = []
            return contP
            
        else:
            pass
    else:
        sensor =[]



def producao():
    if read("Operando")=="True":
        sleep(1)
        return str(round(float(read("ctd_pecs"))/float(read("I")),3)) + "  pcs/s"

def contagem():     
    return read("ctd_pecs")



def estado():
    tags = [["Manual",read("Manoal")],["Parado",read("Parado")],["Parando",read("Parando")],["Reiniciando",read("Reiniciando")],["Pronto",read("Pronto")],["Operando",read("Operando")]]

    for i in tags:
       if i[1]=="True":
          return i[0]

 

def connect(name = "OPC.SimaticHMI.CoRtHmiRTm"):
    objOpc = OpenOPC.client()
    objOpc.connect(name)
    return objOpc

def set_var(tag):
    connect().write((tag,1))
    sleep(0.01)
    connect().write((tag,0))


def read(tag):
    return str(connect()[tag])


def bt_start():
    set_var("Botao_Start_Remoto")
    def reset_color():
        bt_start.configure(bg="gainsboro")
    bt_start.configure(bg = "green")
    janela.after(750,reset_color)

def bt_stop():
    set_var("Botao_Stop_Remoto")
    def reset_color():
        bt_stop.configure(bg="gainsboro")
    bt_stop.configure(bg = "red")
    janela.after(750,reset_color)
def bt_reset():
    set_var("Botao_Reset_Remoto")
    def reset_color():
        bt_reset.configure(bg="gainsboro")
    bt_reset.configure(bg="yellow")
    janela.after(750,reset_color)

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


#------------------------------------------------------------#

state_system = "OPERANDO"
text_operando =  Label(janela, text="", background="gray")
text_operando.place(x=760,y=20)
#------------------------------------------------------------#
def setV():
    text_producao.configure(text=producao())
    text_qtdpecas.configure(text=contagem())

    text_timeProd.configure(text=timer())
    text_operando.configure(text=estado())
    return janela.after(1000,setV)
    


text_producao = Label(janela,text="----", background="gray")
text_producao.place(x=100,y=90)

text_qtdpecas= Label(janela,text="----", background="gray")
text_qtdpecas.place(x=100,y=170)


text_timeProd = Label(janela,text="------", background="gray")
text_timeProd.place(x=100,y=130)


text_operando = Label(janela, text="--", background="gray")
text_operando.place(x=750,y=20)


janela.geometry("900x200")
janela['bg']="gray"
janela.title("SISTEMA SUPERVISORIO MUSCLE FLUID PRESS")

setV()
janela.mainloop()







