# from tema6cn import *
from tkinter import *
from tema6cn import generate_xi_values
from tema6cn import generate_yi_values
from tema6cn import compute_matrix_b
from tema6cn import compute_ai
from tema6cn import compute_Pm_not_x
from tema6cn import *




def maincall():
    x0 = e1.get()
    xn = e2.get()
    print(x0, xn)
    x0 = float(x0)
    xn = float(xn)
    xi = generate_xi_values(x0, xn)
    label3.config(text=("xi " + str(xi)))
    yi = generate_yi_values(xi)
    matrix_b = compute_matrix_b(xi)

    #linear system Ba = f => ai
    ai = compute_ai(matrix_b, yi)

    #compute Pm(x) Horner schema
    Pm_x = compute_Pm_not_x(ai, 3.0)
    #print("Pm_x = ",Pm_x)
    label4.config(text=("Pm_x " + str(Pm_x)))
    # print("|Pm(x)-f(x)|", abs(Pm_x-function_fx(3.0)))
    label5.config(text=("|Pm(x)-f(x)|" + str(abs(Pm_x-function_fx(3.0)))))
    sum = 0
    for i in range(len(xi)):
        Pm_x2 = compute_Pm_not_x(ai, xi[i])
        sum = sum + abs(Pm_x2-yi[i])
    # print("Sum ABS : ", sum)
    label6.config(text=("Sum ABS : "+ str(sum)))


    # # Trigonometric approximation
    # print("\n\nAproximare trigonometrica")
    # x0_t = float(input("enter x0_t:"))
    x0_t = e3.get()
    x0_t = float(x0_t)
    xn_t = e4.get()
    xn_t = float(xn_t)
    # xn_t = float(input("enter xn_t:"))
    t_xi = generate_xi_values(x0_t, xn_t)
    t_yi = generate_yi_trigonometric_values(t_xi)

    d_a = derivata(x0_t)

    Sf_x = compute_Sf_x(d_a, t_xi, t_yi, 1.2)
    # print("Sf_x = ", Sf_x)
    label9.config(text=("Sf_x = " + str(Sf_x)))
    # print("|Sf(x)-f(x)| = ", abs(Sf_x-function_trig_fx(1.2)))
    label10.config(text=("|Sf(x)-f(x)| = " + str(abs(Sf_x-function_trig_fx(1.2)) )))

    plot_f()
    plot_Pm(ai)
    aii_vec=[]
    for i in np.arange (start=0.1, stop=1.5, step=0.2):
        aii_vec.append(compute_Sf_x(d_a, t_xi, t_yi, i))
    plot_Sf(aii_vec)


program = Tk()
program.title("Tema 6 CN")
program.minsize(700,400)
program.resizable(None,None)

label1 = Label(program, text = "Insert x0:",pady = 7)
label1.pack()

e1 = Entry(program,width=25)
e1.pack()

label2 = Label(program,text = "Insert xn:", pady = 7)
label2.pack()

e2 = Entry(program,width=25)
e2.pack()



label3 = Label(program,text = "xi:")
label3.pack()

label4 = Label(program,text = "")
label4.pack()

label5 = Label(program,text = "yi:")
label5.pack()

label6 = Label(program,text = "")
label6.pack()

label7 = Label(program,text = "Enter x0_t:")
label7.pack()
e3 = Entry(program,width = 25)
e3.pack()

label8 = Label(program,text = "Enter xn_t:")
label8.pack()

e4 = Entry(program,width =25)
e4.pack()

label9 = Label(program,text = "")
label9.pack()

label10 = Label(program,text = "")
label10.pack()

button = Button(program,text = "Calcul", command = maincall)
button.pack()




program.mainloop()