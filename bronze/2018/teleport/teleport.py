import sys
answer = None
sys.stdin = open("teleport.in","r")
sys.stdout = open("teleport.out","w")
a,b,x,y = map(int,input().split())
def dist(c,d):
    return abs(c - d)
if dist(a,x) <= dist(a,y):
    prev = "x"
    teledist = dist(a,x) + dist(y,b)
else:
    teledist = dist(a,y) + dist(x,b)

if teledist < dist(a,b):
    answer = teledist
else:
    answer = dist(a,b)
print(answer)
