from itertools import permutations
S, K= map(str,input().split())
permutations = list(permutations(S, int(K)))
permutations.sort()

for i in permutations:
    print("".join(i))