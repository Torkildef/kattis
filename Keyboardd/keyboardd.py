import sys

linje1 = sys.stdin.readline()
linje2 = sys.stdin.readline()

bokstaver =""
x =0
for i in range(len(linje2)):
    try:
        if linje1[x] != linje2[i]:
            if linje2[i] not in bokstaver:
                bokstaver += linje2[i]
        else:
            x+=1
    except:
        if linje2[i] not in bokstaver:
            bokstaver += linje2[i]


print(bokstaver)