marks = []
for i in range(1, 6):
    m = int(input(f"Subject {i}: "))
    marks.append(m)

total = sum(marks)
average = total / 5

print("\n--- Student Result ---")
print("Total Marks =", total, "out of 500")
print("Average Marks =", average)
