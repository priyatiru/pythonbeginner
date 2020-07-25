def print_formatted(number):
    w = len(str(bin(number)).replace('0b',''))
    for i in range(1,number+1):   
        d = str(i).rjust(w,' ')
        b = bin(i)[2:].rjust(w,' ')   ## rjust is used for line alignment
        o = oct(i)[2:].rjust(w, ' ')
        h = hex(i)[2:].rjust(w, ' ').upper()
        print(d, o, h, b)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)