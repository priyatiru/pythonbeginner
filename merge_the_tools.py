def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        line = string[i:i+k]
        seen = set()
        for i in line:
            if i not in seen:
                print(i,end="")
                seen.add(i)
        #prints a new line
        print()


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)