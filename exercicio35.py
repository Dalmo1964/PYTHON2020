# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

lista=[]

palavra = "qqcoisa"

while (palavra !=""):
    palavra = input ('digite qualquer coisa   ')
    lista.append (palavra)

print (lista)

for ele in lista:
    if len(ele) == 4:
        print ( ele )