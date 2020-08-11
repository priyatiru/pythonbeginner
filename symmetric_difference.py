a = int(input())
M = set(list(map(int, input().split())))
b= int(input())
N= set(list(map(int,input().split())))
s = sorted(list(M.difference(N))+list(N.difference(M)))
for i in s:
    print (i)
