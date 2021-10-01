e, f, c = map(int, input().split())

drinked = 0
total = e + f


while c <= total:
    drinked+=1
    total -= (c-1)

print(drinked)



