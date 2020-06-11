#Дан текстовий файл f. Видалити з нього останній рядок, результат записати у
#файл g.
f=open('f.txt', 'w')
f.write("Python\n this\n best\n language\n programming")
f.close()
with open('f.txt') as f:
    text = f.read() 
    items = text.split() 
with open('g.txt', mode='w') as g:
    items = items[:-1]  
    text = '\n'.join(items)
    g.write(text)  
