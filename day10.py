adding = 4 + 3
print(adding)

subtraction = 8 - 9
print(subtraction)

multiplication = 4 * 32
print(multiplication)

division = 50 / 5
print(division)

# a number raised to the power of some number
# in this example we raise 5 to the power of 2
squared = 5**2
print(squared)

# remainder of a division
modulo = 15 % 4
print(modulo)

# whole number division
divisor = 15 // 2
print(divisor)

# Day 10 Challenge
myBill = float(input("What was the bill?: "))
tip = int(input("What percentage do you want to tip?: "))

answerTip = tip / 100 * myBill
totalBill = answerTip + myBill

print(f"You all owe {totalBill}")
numberOfPeople = int(input("How many people?: "))
answer = totalBill / numberOfPeople
print("You all owe", answer)
