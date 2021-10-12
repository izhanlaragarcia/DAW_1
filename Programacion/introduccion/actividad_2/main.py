# print("Bienvenido jugador1 ¿Estas listo para empezar?")
yes = input("Si estas listo pulsa 'y': Sino pulsa 'n': ")
correcto = "70km"

if yes == "y":
    print("Pues empecemos:")
    print("Distancia: 55km")
    print("Tiempo: 30min")

    velocidad = input("¿Aque velocidad iba para tardar ese tiempo?: ")
    correcto = "70"

    if velocidad == correcto:
        print("La velocidad que has dicho es correcta")
    else:
        print("Prueba otra vez...")
elif yes == "n":
    print("Vuelve cuando estes listo!")
else:
    print("Solo pulsa 'y' o 'n'")
