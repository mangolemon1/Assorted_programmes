a = float(input("Enter *a* :"))
b = float(input("Enter *b* :"))
if b >= 0:
    b = " +" + str(b)
c = float(input("Enter *c* :"))
d = float(input("Enter *d* :"))
if d >= 0:
    d = " +" + str(d)
    

print(str(a) + "x" + str(b) + " = " + str(c) + "x" + str(d))
print("--__--__--__--__--__--__--__--__--__--__--__--__--")

b = float(b)
d = float(d)
d = d - b
b = float(b)
b = b - b

print(str(a) + "x" + " = " + str(c) + "x " + str(d))
print("--__--__--__--__--__--__--__--__--__--__--__--__--")

a = a - c
c = c - c

print(str(a) + "x" + " = " + str(d))
print("--__--__--__--__--__--__--__--__--__--__--__--__--")

if a != 1:
    d = float(d)
    d = d/a
    a = a/a
    
print(str(a) + "x" + " = " + str(d))
print("--__--__--__--__--__--__--__--__--__--__--__--__--")

