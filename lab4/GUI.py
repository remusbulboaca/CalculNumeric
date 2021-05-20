from main import *
import tkinter
import time


top = tkinter.Tk()
top.geometry('1000x600')



a,b,c,p,q = get_mtx('res/a4.txt')
f = read_f('res/f4.txt')

L1 = tkinter.Label(top, text="Vector f:", font=("Helvetica", 20, "bold"))
L1.pack(pady=10)

ad = tkinter.Label(top, text="a = " + str(f[:10]) + "...", fg="blue")
ad.pack(pady=10)

L1 = tkinter.Label(top, text="Matricea A", font=("Helvetica", 20, "bold"))
L1.pack(pady=10)

ad = tkinter.Label(top, text="a = " + str(a[:20]) + "...", fg="blue")
ad.pack()
ad = tkinter.Label(top, text="b = " + str(b[:20]) + "...", fg="blue")
ad.pack()
ad = tkinter.Label(top, text="c = " + str(c[:20]) + "...", fg="blue")
ad.pack()

btn1 = tkinter.Button(top, text="Adunare Matrici", font=("Helvetica", 15))
btn1.pack(pady=15, ipady=10,ipadx = 7)

add = tkinter.Label(top, text="", font=("Helvetica", 15, "bold"), fg="green")
add.pack()
add_time = tkinter.Label(top, text="", font=("Helvetica", 15, "bold"), fg="black")
add_time.pack(pady=5)

btn2 = tkinter.Button(top, text="Inmultire Matrici", font=("Helvetica", 15))
btn2.pack(pady=10,ipady=10, ipadx = 7)

ori = tkinter.Label(top, text="", font=("Helvetica", 15, "bold"), fg="green")
ori.pack()
ori_time = tkinter.Label(top, text="", font=("Helvetica", 15, "bold"), fg="black")
ori_time.pack(pady=5)



top.mainloop()