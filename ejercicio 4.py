def finobacci():
    n =0
    a =0
    b =0
    c =0
    aux =0
    while True:
        n = int(input("dame un numero entero positivo: "))
        if n>0:
            break

    a = 1
    for i in range(0,n):
        print("\t"+str(a))
        aux =a
        a +=b
        b = aux


finobacci()
