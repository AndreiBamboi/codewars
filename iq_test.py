def iq_test(numbers):
    numere = numbers.split(' ')
    print(numere)
    print(type(numere))
    odd = []
    even = []
    for x in numere:
        if int(x)%2 == 0:
            even.append(x)
        else:
            odd.append(x)
    print('Numerele impare sunt' , odd)
    print('Numerele pare sunt' , even)
    if len(odd)<len(even) :
        index=numere.index(odd[0])+1
        print(type(index))
        print(index)
        print('Numar dubios este', odd)
        print(type(odd))
    elif len(even)<2:
        print('Numar dubios este', even)
    else:
        return print('Nu am gasit numere dubioase')

iq_test('1 2 2')
