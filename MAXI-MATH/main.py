from cProfile import label
from cgitb import text
from logging import root
import tkinter as tk 
from tkinter import *


#Colors
Button_Start = "#c29713"
Button_App = "#005e3B"

#Functions
def V2():
    
    #V2
    a=Toplevel()
   
    
    a.geometry("500x500")
    a.config( bg="#940c0c")  
    a.title("OPTIONS")  
    label2 = Label(a, text ="CHOOSE WHATEVER YOU NEED", font="chewy",  bg="#940c0c", fg="white")
    label2.place(x=120, y=40)
    boton = tk.Button(a, text="GRAPH I", cursor="hand2", bg=Button_Start, width="9", height="0", relief="flat", font=("Chewy", 12, "bold"), command=V2 )
    boton.place(x=190, y=120)
    boton = tk.Button(a, text="FUNCTIONS G", cursor="hand2", bg=Button_Start, width="11", height="0", relief="flat", font=("Chewy", 12, "bold"), command=V4 )
    boton.place(x=180, y=190)
def V4():   
from glob import glob1
from re import S
import tkinter as t
from tkinter import messagebox
from turtle import bgcolor, color
from matplotlib.pyplot import*
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.animation as anim
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

import numpy as np
from math import*

win=t.Tk()
win.title("Function grapher")
win.geometry("900x800")
win.config(bg="#940c0c")
style.use('fivethirtyeight')
color = "#940c0c"
color1= "#c29713"
fig=Figure( facecolor=color)
ax=fig.add_subplot(111)
cvs=FigureCanvasTkAgg(fig,win)
cvs.draw
cvs.get_tk_widget().pack(side=t.TOP,fill=t.BOTH,expand=1)
tlb=NavigationToolbar2Tk(cvs,win)
tlb.update
tlb.config(background=color1)
tlb.winfo_children()[-2].config(background=color)
cvs.get_tk_widget().pack(side=t.TOP,fill=t.BOTH,expand=1)


rang1=False
rang2=""
rang3=""


fun={"sin":"np.sin","cos":"np.cos","tan":"np.tan","sqrt":"np.sqrt","exp":"np.exp","pi":"np.pi","log":"np.log"}

def reemplaza(p):
    for i in fun:
        if i in p:
            p=p.replace(i,fun[i])
    return p
def animate(i):
    global rang1
    global rang2
    if rang1==True:
        try:
            min=float(rang3[0]);max=float(rang3[1])
            if min<max:
                x=np.arange(min,max,0.01)
                rang2=[min,max]
            else:
                rang1=False
        except:
            messagebox.showwarning("The rank is wrong!!!")
            rang1=False
            entra_var.delete(0,len(entra_var.get()))
    else:
        if rang2!="":
            x=np.arange(rang2[0],rang2[1],0.01)
        else:
            x=np.arange(0,10,0.01)
    try:
        sl=eval(graf_dt)
        ax.clear()
        ax.plot(x,sl)
    except:
        ax.plot()
    ax.axhline(0,color=color1)
    ax.axvline(0,color=color1)
    
    ani.event_source.stop()
def represent():
    global graf_dt
    global rang3
    global rang1
    tx_origl=entra_func.get()
    if entra_var.get()!="":
        rann=entra_var.get()
        rang3=rann.split(",")
        rang1=True
    graf_dt=reemplaza(tx_origl)
    ani.event_source.start()
ani=anim.FuncAnimation(fig,animate,interval=1000)  
show()



bo1=t.Button(win,text="Quit",command=quit,bg=color1, height = 1,width = 20)
bo2=t.Button(win,text="graph",command=represent,bg=color1, height = 1,width = 20)
entra_func=t.Entry(win,width=45)
entra_var=t.Entry(win,width=25)
bo1.pack(side=t.RIGHT, padx=15, pady=20) 
bo2.pack(side=t.RIGHT, padx=15, pady=20)
entra_var.pack(side=t.RIGHT)
entra_func.pack(side=t.LEFT,padx=55, pady=20)


win.mainloop() 

    boton = tk.Button(a, text="DERI-INTE", cursor="hand2", bg=Button_Start, width="11", height="0", relief="flat", font=("Chewy", 12, "bold"), command=V2 )
    boton.place(x=180, y=260)
    boton = tk.Button(a, text="RESOURCES", cursor="hand2", bg=Button_Start, width="11", height="0", relief="flat", font=("Chewy", 12, "bold"), command=V2 )
    boton.place(x=180, y=340)
    label.pack() 
    label2.pack() 
    a.mainloop()  

#V1
ventana = tk.Tk()
ventana.title("LOGIN")
ventana.geometry("360x270+500+50")
ventana.resizable(width=False, height=False)
fondo = tk.PhotoImage(file="Images/idk.png")
fondo1 = tk.Label(ventana, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

#Buttons
boton = tk.Button(ventana, text="Start", cursor="hand2", bg=Button_Start, width="9", height="0", relief="flat", font=("Chewy", 12, "bold"), command=V2 )
boton.place(x=130, y=185)



ventana.mainloop()
