def print_rangoli(size):

    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        if x >= 0:
            line = myStr[size:x:-1]+myStr[x:size]
            print ("--"*x+ '-'.join(line)+"--"*x)


size = int(input())
print_rangoli(size)