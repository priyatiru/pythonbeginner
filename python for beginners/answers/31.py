def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Function to return LCM of two numbers


def lcm(a, b):
    return (a*b) / gcd(a, b)


a = int(input())
b = int(input())
print(gcd(a,b))