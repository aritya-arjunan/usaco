import sys
sys.stdin = open("paint.in","r")
sys.stdout = open("paint.out","w")
line1 = sys.stdin.readline()
line2 = sys.stdin.readline()
a,b = map(int,line1.split())
c,d = map(int,line2.split())
if a <= c:
	x = a
else:
	x = c
if b >= d:
	y = b
else:
	y = d
print(y - x)
