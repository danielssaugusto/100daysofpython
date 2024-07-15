def secure_login():
    print("SECURE LOGIN")
    username = input("Username > ")
    password = input("Password > ")
    if username == "mark" and password == "password":
        print("Welcome Mark!")
    elif username == "suzanne" and password == "suzanne":
        print("Hey there Suzanne!")
    elif username == "jo" and password == "jo":
        print("Yo Jo!")
    else:
        print("Go away!")

while True:
    answer = input("Which an option: \n[1] Secure Login \n[2]")