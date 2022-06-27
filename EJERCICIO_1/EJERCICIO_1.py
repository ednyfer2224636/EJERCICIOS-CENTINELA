cod = int(input("Digite el código del estudiante: "))
nombre = input("Digite el nombre del estudiante: ")
reprobados = 0

if cod !=0:
    nota1 = float(input("Digite la nota del parcial no. 1: "))
    nota2 = float(input("Digite la nota del parcial no. 2: "))
    nota3 = float(input("Digite la nota del parcial no. 3: "))
else:
    print("Fin de la entrada de datos")

while cod != 0:
    notafin = ((nota1 + nota2 + nota3) / 3)
    print("El estudiante", nombre, "con el código", cod, "tiene una nota final de", notafin)

    if notafin < 3.0:
        reprobados = reprobados + 1
        print("Número de estudiantes reprobados:", reprobados)

    cod = int(input("Digite el código del estudiante: "))
    nombre = input("Digite el nombre del estudiante: ")

    if cod != 0:
        nota1 = float(input("Digite la nota del parcial no. 1: "))
        nota2 = float(input("Digite la nota del parcial no. 2: "))
        nota3 = float(input("Digite la nota del parcial no. 3: "))
    
    else:
        print("Fin de la entrada de datos")

print("El número de estudiantes reprobados es", reprobados)

