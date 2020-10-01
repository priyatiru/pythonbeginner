def siminterest(p,r,t):
    return p * ((1 + (r/100))**t)


print(siminterest(int(input()), float(input()), int(input())))
