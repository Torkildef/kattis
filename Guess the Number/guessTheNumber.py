import math

endring = 500
gjett = 500
print(str(gjett))
response = input()

while(response != "correct"):
    endring = endring/2


    if(response == "higher"):
        gjett += endring
        gjett = math.ceil(gjett)
    
    else:
        gjett -= endring
        gjett = math.floor(gjett)
    
    if gjett == 0:
        gjett = 1


    print(gjett)
    response = input()

