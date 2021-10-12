# # Le diremos que nos importe la fecha
from datetime import datetime

# Definiremos las variable con la cantidad de dias que puede tener un mes, pondremos en practica todas las posibilidades
febrero = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
visiesto = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
pares = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
impares = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
meses = [1,2,3,4,5,6,7,8,9,10,11,12]

a = input("Danos el dia: ")
# b = int(input("Danos el mes: "))
# c = int(input("Danos el año: "))

# Condicion de pares
if a == pares:
    b = int(input("Ahora dame un mes: "))
    if b == meses:
        int(input("Por ultimo dame un año: "))
    elif b != meses:
        print("Ponga un formato de mes correto!")
# Condicion de impares
if a == impares:
    b = int(input("Ahora dame un mes: "))
    if b == meses:
        int(input("Por ultimo dame un año: "))
        print(a,"/",b)
    elif b != meses:
        print("Ponga un formato de mes correto!")