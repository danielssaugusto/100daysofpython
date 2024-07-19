def main():
  print("Welcome to the Ultimate Fan Test!")
  interest = input("What are you interested in (e.g., show, movie)? ").strip().lower()

  if interest == "game of thrones":
      print("Ah, Game of Thrones! Let's see if you're a true fan.")
      character = input("Who is known as the King in the North? ").strip().lower()

      if character == "jon snow":
          print("Correct! You know your stuff.")
      else:
          print("Hmm, not quite. Jon Snow is the King in the North!")

  elif interest == "the lord of the rings":
      print("You're a fan of The Lord of the Rings! Here's a question for you.")
      ringbearer = input("Who is the bearer of the One Ring? ").strip().lower()

      if ringbearer == "frodo baggins":
          print("Well done! You've got it right.")
      else:
          print("Oops, that's incorrect. Frodo Baggins is the bearer of the One Ring.")

  elif interest == "star wars":
      print("Star Wars, huh? Let's test your knowledge.")
      jedi_order = input("What are the colors of a Jedi's lightsaber? ").strip().lower()

      if jedi_order == "blue, green, purple, yellow, white":
          print("Impressive! You know your lightsabers.")
      else:
          print("Not quite. A Jedi's lightsaber can have many colors: blue, green, purple, yellow, white.")

  else:
      print("Sorry, I'm not familiar with that interest. Try another one.")

if __name__ == "__main__":
  main()
