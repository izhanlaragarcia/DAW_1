# le diremos al usuario que no pude pasar de 3 cifras a la hora de escbrir el numero:
a = int(input("Primer numero: "))
if a <= 1000:
    print("Este numero es perfecto")
else:
    print("Este numero es de  mas de 3 cifras, coje otro....")
