def answer_user(message):
  user = input(message).capitalize().strip()
  return user


print("Marvel Movie Character Creator")
print("--\n")

while True:
  spiderman = answer_user("Do you like 'hanging around'?: [Yes/No] ")
  if spiderman == "Yes":
    print("Then you're Spider-man!")
    break
  else:
    print("Then you're not Spider-man\n")
    
  korg = answer_user("Do you have a 'gravelly' voice?: [Yes/No] ")
  if korg == "Yes":
    print("Then you're Korg!")
    break
  else:
    print("Then you're not Korg\n")
  
  marvel = answer_user("Do you often feel 'Marvelous'?: [Yes/No] ")
  if marvel == "Yes":
    print("Aha! You're Captain Marvel! Hi!")
    break
  else:
    print("Then you're not Captain Marvel")
