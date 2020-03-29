print("Determinar el mayor de una secuencia de numeros")


def numMayor():
    while True:
        fin = "n"
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))

        if (num1 > num2):
            print("el primer numero: "+str(num1) + " Es mayor")
        else:
            print("el segundo numero: "+str(num2) + " Es mayor")

        respuesta = input("Desea Continuar? Si = s, No = n :")

        if (respuesta == fin):
            break

numMayor()