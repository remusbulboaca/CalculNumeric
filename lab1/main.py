from tangenta import *
import time
from generator import *
from lab1 import *
from tkinter import *
from tkinter import messagebox

def showmach():
    machprecision = ex1()
    label1info.config(text=("Precizia masina pentru operatia:"))
    label2info.config(text=("1.0 + 10^-m != 1.0"))
    label1.config(text=("Precizie masina: " + str(machprecision)))

def showex2():
    label1info.config(text=("Asociativitatea adunarii"))
    label2info.config(text=("(a+b)+c != a+(b+c) \n Unde b si c reprezinta precizia masina"))
    label1.config(text=("Este : " + ex2a()))

def showex2b():
    label1info.config(text=("Asociativitatea inmultirii"))
    label2info.config(text=("(a*b)*c != a*(b*c) \n Unde b si c reprezinta precizia masina"))
    label1.config(text=("Este : " + ex2b()))

def main(n, x):
    return tangenta(n, x)

start_time = time.time()
x = pi_generator2(100)
for i in x:
    print(abs(math.tan(i) - main( 5,i)))
print("--- %s seconds ---" % (time.time() - start_time))

print("--------------------------------")

start_time = time.time()
y = pi_generator(100)
for i in y:
    print(abs(math.tan(i) - 1/main( 5, math.pi/2 - i)))
print("--- %s seconds ---" % (time.time() - start_time))

program = Tk()
program.title("Tema 1 CN")
program.minsize(700,400)
program.resizable(None,None)
buton1 = Button(program,text = "Ex1", fg="blue",command=showmach,pady = 7)
buton1.place(x=20,y=20)
buton2 = Button(program,text = "Ex2a", fg= "yellow", pady = 7, command=showex2)
buton2.place(x=60,y=20)
buton3 = Button(program,text = "Ex2b", fg= "red",pady = 7, command= showex2b)
buton3.place(x=100,y=20)



label1info = Label(program, text = "",pady = 7)
label1info.pack()
label2info = Label(program,text = "")
label2info.pack()
label1 = Label(program,text = "",pady=7)
label1.pack()


program.mainloop()
