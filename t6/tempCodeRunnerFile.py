yi = generate_yi_values(xi)
    # matrix_b = compute_matrix_b(xi)

    # #linear system Ba = f => ai
    # ai = compute_ai(matrix_b, yi)

    # #compute Pm(x) Horner schema
    # Pm_x = compute_Pm_not_x(ai, 3.0)
    # print("Pm_x = ",Pm_x)
    # print("|Pm(x)-f(x)|", abs(Pm_x-function_fx(3.0)))
    # sum = 0
    # for i in range(len(xi)):
    #     Pm_x2 = compute_Pm_not_x(ai, xi[i])
    #     sum = sum + abs(Pm_x2-yi[i])
    # print("Sum ABS : ", sum)


    # # Trigonometric approximation
    # print("\n\nAproximare trigonometrica")
    # x0_t = float(input("enter x0_t:"))
    # xn_t = float(input("enter xn_t:"))
    # t_xi = generate_xi_values(x0_t, xn_t)
    # t_yi = generate_yi_trigonometric_values(t_xi)

    # d_a = derivata(x0_t)

    # Sf_x = compute_Sf_x(d_a, t_xi, t_yi, 1.2)
    # print("Sf_x = ", Sf_x)
    # print("|Sf(x)-f(x)| = ", abs(Sf_x-function_trig_fx(1.2)))