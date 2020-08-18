n_eng=int(input())
arr1=set(map(int,input().split()))
n_french=int(input())
count=0
arr2=set(map(int,input().split()))

intersection= arr1.difference(arr2)
for i in intersection:
    count+=1
    
print(count)
