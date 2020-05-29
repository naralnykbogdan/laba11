#Дан текстовий файл f. Видалити з нього останній рядок, результат записати у
#файл g.
a = []
f = open('file.txt', 'r')
for i in f:  
    a += i
f.close()
while True:  
    b = a.pop()
    if b == '\n':
        break
f = open('file.txt', 'w')  
for k in a:
    f.write(k)
f.close()
g = open('file2.txt', 'w')  
for j in a:
    g.write(j)
g.close()
