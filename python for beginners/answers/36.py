#Write a Python program to add two objects if both objects are an integer type.
x = input()
y = input()
if isinstance(x,int) and isinstance(y,int):
    print(x+y)
else:
    print("Error")
