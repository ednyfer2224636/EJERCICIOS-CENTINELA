n = int(input("Digite un número: "))

par = 0 
impar = 0

while n != 0:
    r = n % 2

    if r == 0:
         par = par + 1
    else:
        impar = impar + 1

    n = int(input("Digite un número: "))

print("La cantidad de números pares es", par, "e impares es", impar)
