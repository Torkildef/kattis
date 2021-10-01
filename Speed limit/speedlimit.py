inn = int(input())

while inn != -1:
    miles= 0
    prev = 0
    for x in range(inn):
        mph, time = input().split()

        miles += int(mph) * (int(time) - prev)
        prev = int(time)

    print(str(miles) + " miles")
    
    inn = int(input())


