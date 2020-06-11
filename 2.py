#Дан двійковий файл f, компоненти якого є дійсними числами. Знайти суму,
#добуток, суму квадратів і квадрат добутку компонентів файлу f, а також останню
#компоненту файлу. Результати записати у файл g.
sum,dob,sum_k,dob_k=0,1,0,1
with open(r"C:\Users\Админ\Desktop\f1.txt", 'rb') as f, open('g1.txt', mode='wb') as g:
        for i in f:
                number = float(i)
                sum += float(i)
                dob *= float(i)
                sum_k += (float(i))**2
                dob_k = dob**2

        a = "Сума чисел = " + str(sum) + "\n"  # конв-ня float в str
        a1 = "Сума квадратів = " + str(sum_k) + "\n"
        a2 = "Добуток = " + str(dob) + "\n"
        a3 = "Квадрат добутку = " + str(dob_k) + "\n"
        a4 = str(number)

        b = a.encode() 
        b1 = a1.encode()
        b2 = a2.encode()
        b3 = a3.encode()
        b4 = a4.encode()

        g.write(b)
        g.write(b1)
        g.write(b2)
        g.write(b3)
        g.write(b4)

