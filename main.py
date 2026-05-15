passwords = {}

while True:
    print("1 Add")
    print("2 Show")
    print("3 Exit")

    choice = input("Choice: ")

    if choice == "1":
        website = input("Website: ")
        password = input("Password: ")

        passwords[website] = password

    elif choice == "2":
        for website, password in passwords.items():
            print(website, password)

    elif choice == "3":
        break
