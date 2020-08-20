T=int(input())
for cases in range(T):
    elem_A=int(input())
    set_A=set(map(int,input().split()))
    elem_B=int(input())
    set_B=set(map(int,input().split()))
    print(set_A.issubset(set_B))