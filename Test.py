c = float(input("Gib"))  # Nur Eingabe Zahl
if c > 0:
    a = 10 + c
elif c < 0:
    a = 10 - c
else:  # Fall, wenn c genau 10 ist
    a = 2
print(a)