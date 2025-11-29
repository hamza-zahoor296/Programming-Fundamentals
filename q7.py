rollNo = int(input("Enter Roll No.: "))
pf = int(input("Enter marks in Programming Fundamentals: "))
ic = int(input("Enter marks in Introduction to Computing: "))
cg = int(input("Enter marks in Computer Graphics: "))

total = pf + ic + cg
average = total / 3

print("\n--- Student Result ---")
print("Roll No.:", rollNo)
print("Programming Fundamentals:", pf)
print("Introduction to Computing:", ic)
print("Computer Graphics:", cg)
print("Total Marks:", total, "out of 300")
print("Average Marks:", average)