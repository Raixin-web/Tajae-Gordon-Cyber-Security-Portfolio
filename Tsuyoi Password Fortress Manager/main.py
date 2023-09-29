from encrypt import AES256
from save import Saver
import os

masterPassCheck = b'DrllP9U0YpzlAHD52OwupGDnjEC2LtW3OKzP9OjV2Qc='


saver = Saver("passwords.txt")
passwords = saver.read()
loggedIn = False

while True:
    if not loggedIn:
        print("Welcome to Tsuyoi Password Fortress(TPF)\n""Please enter your Master Password: ", end="")
        masterPass = input()

        encrypter = AES256(masterPass)

        if encrypter.encrypt("herrscher") != masterPassCheck:
            print("Incorrect Password")
            input()
            continue
        else:
             loggedIn = True

    os.system("cls")

    print("1. Find your Password")
    print("2. Add your Password")
    print("3. Delete your Password")
    print("4. Close Password Manager")

    print("\nChoice: ", end="")
    choice = int(input())

    if choice == 4:
        print("Thanks for choosing TPF as your choice for storing your passwords\n""Until next time, have a great day")
        break

    if choice < 1 or choice > 3:
        print("Choose from numbers 1 to 3 for your prefered option\n""If you wish to close the manager, please choose number 4")
        input()
        continue

    print("What is the name of the application: ", end="")
    app = input()

    if choice == 1:
        for entry in passwords:
            if app in encrypter.decrypt(entry[0]):
                print("\n--------------------------------------------")
                print(f"Name of Application: {encrypter.decrypt(entry[0])}")
                print(f"Password saved: {encrypter.decrypt(entry[1])}")
        input()

    elif choice == 2:
        print("Password: ", end="")
        password = input()

        passwords.append([encrypter.encrypt(app).decode(), encrypter.encrypt(password).decode()])
        saver.save(passwords)

    elif choice == 3:
        for entry in passwords:
            if app == encrypter.decrypt(entry[0]):
                print(f"Are you sure you want to delete '{app}' [y/n]: ", end="")
                confirm = input()

                if confirm == "y":
                    del passwords[passwords.index(entry)]
                    saver.save(passwords)

                break