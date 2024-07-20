# score = input("What was your score on the test?")
# if score >= "80":
#   print("Not too shabby")
# elif score > "70":
#   print("Acceptable.")
# else:
#   print("Dude, you need to study more!")

print("Generation Generator")
print()
year = int(input("What year were you born? "))
if year >= 1925 and year <= 1946:
  print("You are a Traditionalist 🪖")
elif year >= 1947 and year <= 1964:
  print("You are a Baby Boomer")
elif year >= 1965 and year <= 1981:
  print("You are a Generation X")
elif year >= 1982 and year <= 1995:
  print("You are a Millenial")
elif year >= 1996 and year <= 2015:
  print("You are a Generation Z 📱")
else:
  print("You are either too young or too old")
