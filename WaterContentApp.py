from tkinter import *
import requests
import tkinter.messagebox
import sys
import time
from datetime import date

screen = Tk()
screen.geometry ('400x300')
screen.resizable(width=False, height=False)
screen.title('Water Content App')

background_image = PhotoImage(file='chem.gif')
background_label = Label(screen, image=background_image)
background_label.place(relwidth = 1, relheight = 1)

#=====================Content Application==========================#
def is_numeric(s):
    is_digit = True

    for char in s:
        if not char.isdigit() and char not in ["."]:
            is_digit = False
            break

    return is_digit

def perhitungan ():
   try:
       a = InputWeight1.get()
       b = InputWeight2.get()
       c = (((float(a) - float(b)) / float(a)) * 100)
       d = round(c, 4)
       water.set(d)
   except:
       tkinter.messagebox.showwarning('Wrong Input', 'Invalid Data')
       SampleName.set('')
       Weight_1.set('')
       Weight_2.set('')
       water.set('')

def hapus():
    SampleName.set('')
    Weight_1.set('')
    Weight_2.set('')
    water.set('')
    return

def Exit():
    Exit = tkinter.messagebox.askyesno('Exit Confirmation','Do you want to Exit?')
    if Exit > 0:
        screen.destroy()
        return
#PembagianFrame
SampleName = StringVar()
Weight_1 = StringVar()
Weight_2 = StringVar()
water = StringVar()


frame = Frame(screen, bg='#80c1ff',bd=5)
frame.place(relx = 0.5, rely= 0.1, relwidth=0.75, relheight=0.1,anchor='n')

frame1 = Frame(screen, bg='#80c1ff',bd=10)
frame1.place(relx= 0.375, rely= 0.25, relwidth=0.5, relheight=0.6,anchor='n')

frame2 = Frame(screen,bd=10)
frame2.place(relx = 0.75, rely= 0.25, relwidth=0.215, relheight=0.6,anchor='n')

frame3 = Frame(screen)
frame3.place(relx = 0.7, rely= 0.9, relwidth=0.5, relheight=0.05,anchor='n')

powered = Label(frame3,text='Powered by © Lutfi Andre')
powered.place(relheight=1,relwidth=1)

Samp_lbl = Label(frame,text='Sample Identification',bg='#80c1ff')
Samp_lbl.place(relheight=1,relwidth=0.4)
Sample_Name = Entry(frame,textvariable = SampleName)
Sample_Name.place(relx=0.415,relwidth=0.575,relheight=1)

Wght1_lbl = Label(frame1,text='Weight 1',bg='#80c1ff').place(relx=0.05,rely=0.1,relwidth=0.35,relheight=0.1)
InputWeight1 = Entry(frame1,textvariable = Weight_1,font=10)
regWeight1= screen.register(is_numeric)
InputWeight1.config(validate='key',validatecommand=(regWeight1,'%P'))
InputWeight1.place(relx=0.5,rely=0.07,relwidth=0.5,relheight=0.15)

Label (frame1,text = 'Weight 2',bg='#80c1ff').place(relx=0.05,rely=0.3,relwidth=0.35,relheight=0.1)
InputWeight2 = Entry(frame1,textvariable = Weight_2,font=10)
regWeight2= screen.register(is_numeric)
InputWeight2.config(validate='key',validatecommand=(regWeight2,'%P'))
InputWeight2.place(relx=0.5,rely=0.3,relwidth=0.5,relheight=0.15)

resultlabel = Label (frame1,text = 'Water Content (%)',bg='#80c1ff').place(relx=0.1,rely=0.6,relwidth=0.75,relheight=0.1)
Inputwater = Entry(frame1,textvariable = water,state = DISABLED,justify='center',font=18)
Inputwater.place(relx=0.1,rely=0.8,relwidth=0.75,relheight=0.2)

#========================Button=========================#
button = Button(frame2, text='Calculate',bg='#E1F8C3', command=(perhitungan) )
button.place(relx=0,rely=0,relwidth=1,relheight=0.6)

clr_button = Button(frame2,text='Clear',bg='white', command=(hapus) )
clr_button.place(relx=0,rely=0.8,relwidth=1,relheight=0.15)

#Exit_button = Button(frame2,text='Exit', command=(Exit) )
#Exit_button.grid(row=4,column=2,padx=20,sticky=N)

screen.mainloop()