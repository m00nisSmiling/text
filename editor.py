#!/usr/bin/python3
from tkinter import *
from tkinter import filedialog as f
import subprocess

b = Tk()
b.configure(bg='#2c3e4c')
b.title('T3XT 3D!T0R 8Y m00nIsSmiling')
f0 = Frame(b,bg='#2c3e4c')
f0.pack(side=LEFT,padx=7)

f1 = Frame(b,bg='#2c3e4c')
f1.pack(pady=10)
def s4v3():
 b1 = f.asksaveasfile()
 b1.write(texti.get(0.0,END))

def op3n():
 b2 = f.askopenfile()
 texti.delete(0.0,END)
 texti.insert(END,b2.read())

def d3l3t():
 texti.delete(0.0,END)
 
Button(f0,text='54V3',command=s4v3,width=8,height=1,font='Verdana 14 bold',bg='#2c3e4c',fg='white',highlightbackground='#1338Be',highlightthickness=2,activebackground='#1338Be',activeforeground='#151E3D').pack(side=TOP,pady=5)
Button(f0,text='0P3N',command=op3n,width=8,height=1,font='Verdana 14 bold',bg='#2c3e4c',fg='white',highlightbackground='yellow',highlightthickness=2,activebackground='yellow',activeforeground='#151E3D').pack(side=TOP,pady=5)
Button(f0,text='CL34R',command=d3l3t,width=8,height=1,font='Verdana 14 bold',bg='#2c3e4c',fg='white',highlightbackground='red',highlightthickness=2,activebackground='red',activeforeground='#151E3D').pack(side=TOP,pady=5)
texti = Text(f1,font='Verdana 10 bold',width=150,height=45,bg='#2c3e4c',fg='lime',insertbackground='red',insertwidth=5,selectbackground='white',selectforeground='red',highlightbackground='lime',highlightthickness=2,relief='solid')

texti.pack(side=LEFT,padx=5)




b.mainloop()
