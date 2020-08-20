k=int(input())
rooms = input().split()
single=set()
multiple=set()
for room in rooms:
    if room not in single:
        single.add(room)
    else:
        multiple.add(room)
print(single.difference(multiple).pop())