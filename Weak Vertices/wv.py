import sys


aLinjer = int(sys.stdin.readline())
while aLinjer > -1:
    noder = []
    for i in range(aLinjer):
        linje = sys.stdin.readline()
        node = linje.strip().split()
        nodeAtributter = []
        for j in range(len(node)):
            if int(node[j]) == 1:
                nodeAtributter.append(j)
        
        noder.append(nodeAtributter)
    weak = []
    for i in range(aLinjer):
        weak.append(True)
    for i in range(len(noder)):
        if weak[i]:
            for a in noder[i]:
                for x in noder[a]:
                    if x in noder[i]:
                        weak[i] = False
                        weak[x] = False
                        weak[a] = False
    weakL = []
    for i in range(len(weak)):
        if weak[i]:
            weakL.append(i)
    print(*weakL)

    
    aLinjer = int(sys.stdin.readline())



                   