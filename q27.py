hours, minutes, seconds = map(int, input("Enter time (hours minutes seconds): ").split())
totalSeconds = (hours * 3600) + (minutes * 60) + seconds

print("\n--- Time Conversion ---")
print("Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)
print("Total Seconds =", totalSeconds)
