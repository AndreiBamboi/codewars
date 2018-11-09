def findNB(m):
    if 1 ** 3 == m:
        return 1
    else:
        n = 2
        volume = 1
        while volume < m:
            volume = volume + n ** 3
            if volume == m:
                print(n)
                return n
            else:
                print(n)
                n = n + 1

                continue
        return -1

findNB(91716553919377)