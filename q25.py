import math

a, b, c = map(float, input("Enter the three sides of the triangle: ").split())
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("\n--- Triangle Area ---")
print("Sides:", a, b, c)
print("Semi-perimeter (s) =", s)
print("Area =", area)
