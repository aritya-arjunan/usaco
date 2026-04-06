import sys
sys.stdin = open("promote.in","r")
sys.stdout = open("promote.out","w")
input = sys.stdin.readline
print = sys.stdout.write
bronze = list(map(int,input().split()))
silver = list(map(int,input().split()))
gold = list(map(int,input().split()))
platinum = list(map(int,input().split()))
gtop = platinum[1] - platinum[0]
stog = gtop + gold[1] - gold[0]
btos = stog + silver[1] - silver[0]
print(f"{btos}\n{stog}\n{gtop}")
