from itertools import combinations
S, K= map(str,input().split())
for i in range(1, int(K)+1):
    for j in combinations(sorted(S), i):
        print ("".join(j))