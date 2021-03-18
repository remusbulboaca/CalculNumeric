import time
from tkinter import *
from main import *



def verfica_adunare(matriceA, matriceB, label, t):
    start = time.time()
    res = verificare_adunare_main(matriceB,matriceA)
    timp = time.time() - start
    label.config( text = str(res))
    t.config(text="Timp de rulare: " + str(timp))

def verfica_inmultire(matriceB, label, t):
    start = time.time()
    res = verificare_inmultire_main(matriceB)
    timp = time.time() - start
    label.config( text = str(res))
    t.config(text="Timp de rulare: " + str(timp))


def gui(top):
    b = matriceB
    a = matriceA
    operations = Matrix_operations()

    a.citire_eficienta_a(a, "res/a.txt")
    b.citire_eficienta_b(b, "res/b.txt")

    aplusb = matriceA
    aplusb.citire_eficienta_a(aplusb, "res/aplusb.txt")

    L1 = Label(top, text="Matricea A", font=("Helvetica", 20, "bold"))
    L1.pack(pady=10)

    ad = Label(top, text="a = " + str(a.a[:2]) + "...", fg="blue")
    ad.pack(pady=10)

    L1 = Label(top, text="Matricea B", font=("Helvetica", 20, "bold"))
    L1.pack(pady=10)

    ad = Label(top, text="a = " + str(b.a[:20]) + "...", fg="blue")
    ad.pack()
    ad = Label(top, text="b = " + str(b.b[:20]) + "...", fg="blue")
    ad.pack()
    ad = Label(top, text="c = " + str(b.c[:20]) + "...", fg="blue")
    ad.pack()

    btn1 = Button(top, text="Adunare Matrici", font=("Helvetica", 15),command=lambda: verfica_adunare(a, b,add, add_time))
    btn1.pack(pady=15, ipady=10,ipadx = 7)

    add = Label(top, text="", font=("Helvetica", 15, "bold"), fg="green")
    add.pack()
    add_time = Label(top, text="", font=("Helvetica", 15, "bold"), fg="black")
    add_time.pack(pady=5)

    btn2 = Button(top, text="Inmultire Matrici", font=("Helvetica", 15), command=lambda: verfica_inmultire(b,ori, ori_time))
    btn2.pack(pady=10,ipady=10, ipadx = 7)

    ori = Label(top, text="", font=("Helvetica", 15, "bold"), fg="green")
    ori.pack()
    ori_time = Label(top, text="", font=("Helvetica", 15, "bold"), fg="black")
    ori_time.pack(pady=5)


top = Tk()
top.geometry('1000x600')
gui(top)
top.mainloop()
