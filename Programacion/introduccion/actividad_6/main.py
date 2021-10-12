# Vamos a culcular el 21% de IVA de los objetos que no lo tienen:
cosa = input("Dime que producto quieres vender: ")
precio = int(input("Dime el precio de tu producto: "))
ambas = print("Informacion:" "\
    ","Objeto:",cosa,"\
        " "Precio:",precio,"€")
# Operación
iva = precio * 0.21
total = iva + precio
print("El precio de tu producto conn el 21% de IVA serian: ",total)

