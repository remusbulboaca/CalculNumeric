from main import *
import tkinter as Tk
import time


top = Tk()
top.geometry('1000x600')



a,b,c,p,q = get_mtx('res/a4.txt')
f = read_f('res/f4.txt')

L1 = Label(top, text="Vector f:", font=("Helvetica", 20, "bold"))
L1.pack(pady=10)

ad = Label(top, text="a = " + str(f[:10]) + "...", fg="blue")
ad.pack(pady=10)

L1 = Label(top, text="Matricea A", font=("Helvetica", 20, "bold"))
L1.pack(pady=10)

ad = Label(top, text="a = " + str(a[:20]) + "...", fg="blue")
ad.pack()
ad = Label(top, text="b = " + str(b[:20]) + "...", fg="blue")
ad.pack()
ad = Label(top, text="c = " + str(c[:20]) + "...", fg="blue")
ad.pack()

btn1 = Button(top, text="Adunare Matrici", font=("Helvetica", 15))
btn1.pack(pady=15, ipady=10,ipadx = 7)

add = Label(top, text="", font=("Helvetica", 15, "bold"), fg="green")
add.pack()
add_time = Label(top, text="", font=("Helvetica", 15, "bold"), fg="black")
add_time.pack(pady=5)

btn2 = Button(top, text="Inmultire Matrici", font=("Helvetica", 15))
btn2.pack(pady=10,ipady=10, ipadx = 7)

ori = Label(top, text="", font=("Helvetica", 15, "bold"), fg="green")
ori.pack()
ori_time = Label(top, text="", font=("Helvetica", 15, "bold"), fg="black")
ori_time.pack(pady=5)



top.mainloop()