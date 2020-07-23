def split_and_join(line):
    x=line.split()
    return "-".join(x)

line = input()
result = split_and_join(line)
print(result)
