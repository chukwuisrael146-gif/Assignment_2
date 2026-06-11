try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    sub1 = a - b
    sub2 = b - a

    if a > b:
        print(f"A - B = {sub1}")
    elif a < b:
        print(f"B - A = {sub2}")
    else:
        print("A and B are the same numbers")

except ValueError:
    print("Those are not numbers")