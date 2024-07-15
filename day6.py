def secure_login():
    print("\nSECURE LOGIN")
    while True:
        username = input("Username > ")
        password = input("Password > ")
        if username == "mark" and password == "password":
            print("Welcome Mark!\n")
            break
        elif username == "suzanne" and password == "suzanne":
            print("Hey there Suzanne!\n")
            break
        elif username == "jo" and password == "jo":
            print("Yo Jo!\n")
            break
        else:
            print("Go away!\n")
            break

    while True:
        continueApp = input("Do you like to continue? [Yes/No]").lower().strip()
        if continueApp == "yes":
                print("\nSECURE LOGIN")
                while True:
                    username = input("Username > ")
                    password = input("Password > ")
                    if username == "mark" and password == "password":
                        print("Welcome Mark!\n")
                        break
                    elif username == "suzanne" and password == "suzanne":
                        print("Hey there Suzanne!\n")
                        break
                    elif username == "jo" and password == "jo":
                        print("Yo Jo!\n")
                        break
                    else:
                        print("Go away!\n")
                        break
        elif continueApp == "no":
            break
        else:
            print("Choose a correct option.")


def seasons():
    season = input("\nWhat is your favorite season? ")
    if season == "spring":
        print("Ah! The birds are chirping and flowers blooming.\n")
    elif season == "summer":
        print("Catch some sun and cool off with a lemonade.\n")
    elif season == "autumn":
        print("The leaves are changing and the air is crisp. Enjoy!\n")
    elif season == "winter":
        print("Stay warm by the fire and watch the snow fall.\n")
    else: 
        print("I don't know that season. Please try again.\n")


def main():
    while True:
        answer = input("Which an option: \n[1] Secure Login \n[2] Season\n").lower().strip()
        if answer == "1" or answer == "secure login":
            secure_login()
        elif answer == "2" or answer == "season":
            seasons()
        else:
            print("Try again")


if __name__ == "__main__":
    main()