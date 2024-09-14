a = float(input())
b = float(input())
c = float(input())

if a + b >= c and c + a >= b and c + b >= a:
    if a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or c**2 + a**2 == b**2:
        print("to jest tr")
    elif a == b == c:
        print("to jest tr rownoramienny")
    else:
        print("to jest tr r boczny")
else:
    print("to nie jest tr")