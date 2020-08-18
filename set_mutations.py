n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N): 
    command=input().split()   
    if command[0]=="intersection_update":
        s.intersection_update(list(map(int,input().split())))
    elif command[0]=="update":
        s.update(list(map(int,input().split())))
    elif command[0]=="symmetric_difference_update":
        s.symmetric_difference_update(list(map(int,input().split())))
    elif command[0]=="difference_update":
        s.difference_update(list(map(int,input().split())))
print(sum(s))