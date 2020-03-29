numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))

def producto(numero1, numero2):
    aux = 0
    for i in range(0,numero2):              
        aux = aux+numero1
        print("El resultado "+str(i)+" es: "+str(aux))

    #mostramos el resultado del producto
    print("el producto es: "+str(aux))


producto(numero1, numero2)