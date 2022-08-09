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
    boton = tk.Button(a, text="FUNCTIONS G", cursor="hand2", bg=Button_Start, width="11", height="0", relief="flat", font=("Chewy", 12, "bold"), command=V2 )
    boton.place(x=180, y=190)
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