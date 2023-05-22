import tkinter as tk
from tkinter import messagebox as me        
windown=tk.Tk()

windown.title('BMI工具')
windown.geometry('200x200')
windown.resizable(False,False)

arr={'1':"過胖",'2':"過輕",'3':"正常"}
def com():
    height = float(hing_intput.get())
    weight = float(wing_input.get())
    bmi = round(weight / ((height/100)**2), 2)
    if bmi<18.50:
        out.config(text=name_inup.get()+" BMI is "+str(bmi))
        me.showinfo('showinfo',arr['1'])
    elif 24.00>bmi>=18.50:
        out.config(text=name_inup.get()+" BMI is "+str(bmi))
        me.showinfo('showinfo',arr['3'])
    elif 24.00<bmi<=27.00:
        out.config(text=name_inup.get()+" BMI is "+str(bmi))
        me.showinfo('showinfo',arr['2'])
    print(bmi)
name_la=tk.Label(windown,text='你的名字')
name_la.pack()
name_inup=tk.Entry(windown)
name_inup.pack()
hing_la=tk.Label(windown,text='你的身高多少')
hing_la.pack()
hing_intput=tk.Entry(windown)
hing_intput.pack()
wing_la=tk.Label(windown,text='你的體重多少')
wing_la.pack()
wing_input=tk.Entry(windown)
wing_input.pack()
out=tk.Label(windown)
out.pack()
intput=tk.Button(windown,text="計算",command=com)
intput.pack()
windown.mainloop()
