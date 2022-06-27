ch = int(input("Digite el valor del cheque: "))
tb1 = 0
tb2 = 0
tb3 = 0

while ch != 0:
    if (ch % 100) == 0:
        b1 = int(ch / 10000)
        r = ch - b1 * 10000
        b2 = int(r / 2000)
        r = r - b2 * 2000
        b3 = int(r / 100)
        tb1 = tb1 + b1
        tb2 = tb2 + b2
        tb3 = tb3 + b3
        print("Los billetes que le devolvemos en función del valor del cheque con el valor de", "$",ch, "son", b1, "de $10000,", b2, "de $2000, y", b3, "de $100")
        ch = int(input("Digite el valor del cheque: "))
    else: 
        print("No le podemos cambiar el billete")
    ch = int(input("Digite el valor del cheque: "))

print("El total de billetes de $10000, $2000 y $100 que se dieron el día de hoy, son, respectivamente", tb1, tb2, tb3)