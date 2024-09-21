import math
from math import sqrt

PI = math.pi
# print(PI)

print(f"a - bryly | b - figury plaskie")
co_mam_zrobic = input()
if co_mam_zrobic == "a":
    print(f"a - szescian | b - prostopadloscian | c - graniastoslup | d - ostroslup | e - walec | f - stozek | g - kula")
    co_mam_zrobic = input()
    if co_mam_zrobic == "a":
        a = float(input())
        print(f"Pole szescianu = {6*a**2}")
    elif co_mam_zrobic == "b":
        a = float(input())
        b = float(input())
        c = float(input())
        print(f"Pole prostopadloscianu = {2*a*b+2*a*c+2*b*c}")
    elif co_mam_zrobic == "c":
        pp = float(input())
        pb = float(input())
        print(f"Pole graniastoslupa = {2*pp+pb}")
    elif co_mam_zrobic == "d":
        pp = float(input())
        pb = float(input())
        print(f"Pole ostrolupa = {pp+pb}")
    elif co_mam_zrobic == "e":
        r = float(input())
        h = float(input())
        print(f"Pole walca = {2*PI*r**2+2*PI*r*h}")
    elif co_mam_zrobic == "f":
        r = float(input())
        l = float(input())
        print(f"Pole stozka = {PI*r**2+PI*r*l}")
    elif co_mam_zrobic == "g":
        r = float(input())
        print(f"Pole kuli = {4*PI*r**2}")
elif co_mam_zrobic == "b":
    print(f"a - kwadrat | b - prostokat | c - rownoleglobok | d - trapez | e - trojkat | f - trojkat rwnbcz | g - kolo | h - romb | i - ROMB")
    co_mam_zrobic = input()
    if co_mam_zrobic == "a":
        a = float(input())
        print(f"Pole kw = {a*a}")
    elif co_mam_zrobic == "b":
        a = float(input())
        b = float(input())
        print(f"Pole prostokata = {a*b}")
    elif co_mam_zrobic == "c":
        a = float(input())
        h = float(input())
        print(f"Pole rownolegloboku = {a*h}")
    elif co_mam_zrobic == "d":
        a = float(input())
        b = float(input())
        h = float(input())
        print(f"Pole trapezu = {(a+b)*h/2}")
    elif co_mam_zrobic == "e":
        a = float(input())
        h = float(input())
        print(f"Pole trojkata = {1/2*a*h}")
    elif co_mam_zrobic == "f":
        a = float(input())
        print(f"Pole trojkata rwnbcz = {a**2*sqrt(3)/4}")
    elif co_mam_zrobic == "g":
        r = float(input())
        print(f"Pole kola = {PI*r**2}")
    elif co_mam_zrobic == "h":
        a = float(input())
        h = float(input())
        print(f"Pole rombu = {a*h}")
    elif co_mam_zrobic == "i":
        e = float(input())
        f = float(input())
        print(f"Pole ROMBU = {e*f/2}")
else:
    print("Nie ma takiej komendy")