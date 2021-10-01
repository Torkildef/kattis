ant = int(input())

cir = map(int, input().split())

for x in range(ant-1):
    print(cir[0]/cir[x+1])
