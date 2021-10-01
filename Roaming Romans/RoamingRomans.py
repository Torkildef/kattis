import sys

tall = float(sys.stdin.readline())

nytall = tall*1000 *(5280/4854)

print(round(nytall))