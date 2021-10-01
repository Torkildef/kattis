import sys

antall = int(sys.stdin.readline())
num = 1

while antall != 0:
    print("SET", num)
    num+=1

    navnBak = []
    navnForan = []

    teller = 2
    for x in range(antall):
        linje = sys.stdin.readline()
        if teller%2 == 0:
            navnForan.append(linje)
        else:
            navnBak.append(linje)

        teller+=1

    for navn in navnForan:
        print(navn)

    for navn in reversed(navnBak):
        print(navn)
    
    antall = int(sys.stdin.readline())




