def divisors(integer):
    global lista
    if integer>1:
        lista = []
        for i in range(2,integer-1):
            if integer%i == 0:
                lista.append(i)
    else:
        print("Numar negativ")
    print(lista)

divisors(25)
