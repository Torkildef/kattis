import sys

runder = int(sys.stdin.readline())
liste = [[],[]]

def settInn(liste, radius, farge):
    for i in range(len(liste[0])):
        if radius < liste[0][i]:
            liste[0].insert(i, radius)
            liste[1].insert(i, farge)
            return liste
    liste[0].append(radius)
    liste[1].append(farge)

    return liste


for _ in range(runder):
    linjer = sys.stdin.readline().split(" ")

    try:
        farge = linjer[0]
        radius = int(linjer[1])

    except:
        radius = int(linjer[0])/2
        farge = linjer[1]
    
    liste = settInn(liste, radius, farge)

for farge in liste[1]:
    print(farge)
    
