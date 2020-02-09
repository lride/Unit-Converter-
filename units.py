# Ask user for input:
a = float(input("Enter # of centimeters to convert", ))

# Build conversion computation for inches through a new variables i
i = a*(0.394/1)

# Build computation for feet through new variable f
f = i*(1/12)

# Show results
print(a, "is roughly",round(i, 1), "inches")
print("and roughly", round(f, 1), "feet")
