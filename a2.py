a = input("Enter a number ")
b = input("Enter a number ")

# conveting input to integer

a = int(a)
b = int(b)

# performing the the subtraction
sub1 = a - b
sub2 = b - a

result1 = sub1
result2 = sub2

# using if statements to write our subtraction condition

if a > b:
    print(f"A - B = {result1}")
elif a < b:
    print(f"B - A = {result2}")
elif a == b:
    print("A and B are the same numbers")