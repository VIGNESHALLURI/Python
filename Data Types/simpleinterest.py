# Simple Interest Calculator

# Input principal, rate, and time from the user
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))

# Calculate simple interest
simple_interest = (principal * rate * time) / 100

# Display the results
print(f"Simple Interest = {simple_interest}")