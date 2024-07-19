name = input("What is your name? ").capitalize().strip()
print(f"Hello {name}")
favorite = input("What is your favorite thing? ").lower().strip()

while True:
    day = input("What day of the week is it? ").lower().strip()
    if day == "monday":
        print(f"Monday is the worst day of the week, but at least you have {favorite} to do!")
        if name[0] == "M":
            print("I hope you're not like Monday")
        break
    elif day == "tuesday":
        print(f"Tuesday is the second worst day of the week, but at least you have {favorite} to do!")
        break
    elif day == "wednesday":
        print(f"I'm halfway through the week, proud of all I've accomplished so far. I'm resilient and later I'll indulge in {favorite}")
        break
    elif day == "thursday":
        print(f"Thursday is the fourth worst day of the week, but at least you have {favorite} to do!")
        break
    elif day == "friday":
        print(f"Friday is the best day of the week, but at least you have {favorite} to do!")
        break
    elif day == "saturday":
        print(f"Saturday is the second best day of the week, but at least you have {favorite} to do!")
        break
    elif day == "sunday":
        print(f"Sunday is the worst day of the week, but at least you have {favorite} to do!")
        break
    else:
        print("That is not a day of the week!")
        continue

  