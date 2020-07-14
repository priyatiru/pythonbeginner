n=int(input())
arr=map(int,input().split())
arr=list(arr)
arr.sort(reverse=True)
for i in range(1,n):
    if(arr[0]==arr[i]):
        continue
    print(arr[i])
    break
