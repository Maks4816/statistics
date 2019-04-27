# мода, медиана, среднее значение, колво
para = {}

# ввод xi и xi
def inp_xi_ni(para):
    try:
        xi = int(input("Введите xi: "))
        ni = int(input("Введите ni: "))
    except:
        print("Похоже, вы ввели букву. Введите число, пожалуйста")
    else:
        if xi not in para:
            para[xi] = ni
        else:
            print("xi уже имеется, введите другое")
        return para

# мода
def moda(para):
    values = para.values()
    true_values = [item for item in values]
    bigger = max(true_values)
    try:
        chislo = true_values.count(bigger)
    except:
        print("Похоже, вы не ввели значения xi и ni. Введите эти числа в пункте 1")
    else:
        reverse_para = {value: key for key, value in para.items()}
        if chislo >= 2:
            return "Моды нету"
        else:
            return reverse_para[bigger]

# медиана
def mediana(para):
    try:
        values = para.values()
        true_values = [item for item in values]
        spisok = [k for k, v in para.items() for i in range(v)]
        n = 0
        for i in true_values:
            n = n + i
        if (n % 2) != 0:
            polozh_mediana = int((n + 1) / 2)
            true_mediana = spisok[polozh_mediana]
        else:
            polozh_mediana = round(((n / 2) + ((n / 2) + 1)) / 2)
            true_mediana = spisok[polozh_mediana]
    except:
        print("Похоже, вы не ввели значения xi и ni. Введите эти числа в пункте 1")
    else:
        return true_mediana

# среднее значение
def average(para):
    try:
        values = para.values()
        true_values = [item for item in values]
        n = 0
        for i in true_values:
            n = n + i
        mnozh = [key * value for key, value in para.items()]
        summa = 0
        for item in mnozh:
            summa += item
        averagee = round(summa / n, 1)
    except:
        print("Похоже, вы не ввели значения xi и ni. Введите эти числа в пункте 1")
    else:
        return averagee


# основной цикл
choice = None
while choice != "0":
    print("""
0 - Выход
1 - Добавить значения xi и ni
2 - Вычислить моду
3 - Вычислить медиану
4 - Вычислить среднее значение
        """)
    choice = input("Ваш выбор: ")
    if choice == "0":
        print("Удачи!")
    elif choice == "1":
        inp_xi_ni(para)
        print("В список добавлены сделующие значения: \n", para)
    elif choice == "2":
        print("\nЗначение моды:", moda(para))
    elif choice == "3":
        print("\nЗначение медианы:", mediana(para))
    elif choice == "4":
        print("\nСреднее значение:", average(para))
