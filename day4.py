hates = input("What do you hate? ")
likes = input("What do you like? ")
family = input("What is the name of your family member? ").capitalize()
friend = input("What is the name of your friend? ").capitalize()
print("I hate", hates, "and I like", likes, "and my family member's name is", family, "and my friend's name is", friend)
print()
print()
print("=== Your Adventure Simulator ===")
print("""
Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!""")
print()
name = input("What is your name? ").capitalize()
enemy = input("What is your worst enemy’s name? ").capitalize()
superpower = input("What is your superpower? ")
live = input("Where do you live? ").capitalize()
food = input("What is your favorite food? ")
print()
print(f"Hello {name}! Your ability to {superpower} will make sure you never have to look at {enemy} again. Go eat {food} as you walk down the streets of {live} and use {superpower} for good and not evil!")
answer = input(f"Are you ready to start your adventure, {name}? [yes/no]").lower()
if answer == "yes":
  print(f"Great! Let's get started, {name}!")
else:
  print(f"Too bad, {name}! Let's get started!")
  print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")

# Sneaky Extra Skill
# You can jazz things up even more by changing the color of the text. Wow. We're quickly approaching the quality of output of a computer from 1981! 😬

# How does it work?
# It's all just print statements, but using special codes that tell your console to start printing everything after this point in the new color.
# You will need to reset if you want to go back and change it in previous lessons.
 

 

# The somewhat random characters in the print argument are telling the computer to change the color of the next text output to whichever color you pick.
# You must add the number from the table below.
 

# Color	    Value
# Default	0
# Black	    30
# Red	    31
# Green	    32
# Yellow	33
# Blue	    34
# Purple	35
# Cyan	    36
# White	    37

# Example
# print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")
# Use that to add extra spice to your authorial masterpiece!