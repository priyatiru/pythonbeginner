n=int(input())
list=[]
for i in range(n):
    s=input().split()
    len_s=len(s)
    for i in range(1,len_s):
        s[i]=int(s[i])
    if s[0]=="append":
        list.append(s[1])
    elif s[0]=="remove":
        list.remove(s[1])
    elif s[0]=="insert":
        list.insert(s[1],s[2])
    elif s[0]=="pop":
        list.pop()
    elif s[0]=="count":
        print(list.count(s[1]))
    elif s[0]=="sort":
        list.sort()
    elif s[0]=="reverse":
        list.reverse()
    elif s[0]=="print":
        print(list)
