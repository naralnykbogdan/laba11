#Дан двійковий файл f, компоненти якого є дійсними числами. Знайти суму,
#добуток, суму квадратів і квадрат добутку компонентів файлу f, а також останню
#компоненту файлу. Результати записати у файл g.
sum_1 = 0
p_1 = 1
sum_2 = 0
p_2 = 1
count = 0
q = 0
with open("first.txt", 'rb') as f, open("second.txt", 'wb') as g:
    for item in f:  
        q -= 1
        last_element = float(item) #формули
        sum_1 += float(item)
        p_1 *= float(item)
        sum_2 += (float(item))
        p_2 *= float(item)
        a = p_2
        count += 1
with open("first.txt", 'rb') as f, open("second.txt", 'wb') as g:  
    for item in f:  

        s = "Сума чисел:" + str(sum_1) + "\n"            #конвертування цілого числа в строку
        bt = s.encode()  
        g.write(bt)  # записуєм у файл

        s = "Сума квадратів чисел:" + str(sum_2) + "\n"  #конвертування цілого числа в строку
        bt = s.encode()  
        g.write(bt)  # записуєм у файл

        s = "Добуток чисел:" + str(p_1) + "\n"            #конвертування цілого числа в строку
        bt = s.encode()  
        g.write(bt)  # записуєм у файл

        s = "Квадрат добутку чисел:" + str(a) + "\n"      #конвертування цілого числа в строку
        bt = s.encode() 
        g.write(bt)  # записуєм у файл

        s = "Останній елемент:" + str(last_element)  
        bt = s.encode()  
        g.write(bt)  # записуєм у файл
        break
