import math
print ("ax^2 + bx + c = 0")
a = float(input ("a = "))
b = float(input ("b = "))
c = float(input ("c = "))
d = b ** 2-4 * a * c
print("discriminant = ",d)
x1 = (-b+math.sqrt (d))/(2 * a)
x2 = (-b-math.sqrt (d))/(2 * a)
print("X1 = ",x1)
print("X2 = ",x2)