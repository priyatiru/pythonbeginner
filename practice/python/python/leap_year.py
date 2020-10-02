def is_leap(year):
    if year % 4 == 0:
        leap = True
        if year % 400 == 0:
            leap = True
        elif year % 100 == 0:
            leap = False
    else:
        leap = False
    return leap


print(is_leap(int(input("Enter a year to check for Leap year: "))))
