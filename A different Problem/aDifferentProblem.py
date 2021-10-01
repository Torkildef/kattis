import sys

for line in sys.stdin.readlines():
    a,b = map(int, line.split())
    if(a>b):
        print(int(a)-int(b))
    
    else:
        print(int(b)-int(a))
