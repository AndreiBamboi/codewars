def digital_root(n):
    x = sum(int(digit) for digit in str(n))
    print(type(str(n)))
    print(int(str(n)))
    if x < 10:
        print(x)
        return x
    else:
        #print(x)
        return digital_root(x)
digital_root(235)