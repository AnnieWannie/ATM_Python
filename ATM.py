def atm_opener():
    fake_pin = 1117
    pin_attempts = 3
    user_pin = 0
    print("Hello and welcome to the Humber bank terminal")
    while True:
        try:
            user_pin = int(input("Please enter your PIN: "))
        except ValueError:
            print("Enter a valid PIN input\n")
        if user_pin == fake_pin:
            break
        else:
            pin_attempts -= 1
            print(f"Pin incorrect. {pin_attempts} attempts remaining")
            assert (pin_attempts != 0), "Too many incorrect PIN attempts."


def display_balance(balance):
    print(f"\nCurrent balance is ${balance:.2f}")


def display_withdraw(balance):
    user_choice = -1
    amount = 0
    while user_choice != int:
        print("\nWithdrawal Amount")
        print("1. $20.00")
        print("2. $40.00")
        print("3. $60.00")
        print("4. $80.00")
        print("5. $100.00")
        print("6. Custom amount")
        print("7. Return to main menu")
        try:
            user_choice = int(input())
        except ValueError:
            print("Invalid response type")
        finally:
            if 1 <= user_choice <= 7:
                break
            else:
                print("Please select a valid option")
    if user_choice == 1:
        if balance - 20 > 0:
            balance -= 20
            return balance
        else:
            print("Non-sufficient funds")
    if user_choice == 2:
        if balance - 40 >= 0:
            balance -= 40
            return balance
        else:
            print("Non-sufficient funds")
    if user_choice == 3:
        if balance - 60 >= 0:
            balance -= 60
            return balance
        else:
            print("Non-sufficient funds")
    if user_choice == 4:
        if balance - 80 >= 0:
            balance -= 80
            return balance
        else:
            print("Non-sufficient funds")
    if user_choice == 5:
        if balance - 100 >= 0:
            balance -= 100
            return balance
        else:
            print("Non-sufficient funds")
    if user_choice == 6:
        try:
            amount = float(input("Enter withdrawal amount: "))
            amount = round(amount, 2)
        except ValueError:
            print("Invalid withdrawal input")
        if balance - amount >= 0:
            balance -= amount
            return balance
        else:
            print("Non-sufficient funds")
    if user_choice == 7:
        return balance
    return balance


def display_deposit(balance):
    print("Enter deposit amount")
    try:
        balance += float(input())
    except ValueError:
        print("Invalid deposit input")
    return balance


def display_exit():
    print("\nThank you for banking with Humber")
    print("Returning card...")
    exit()


def atm_main_menu():
    user_balance = 700.00
    menu_choice = 0
    while True:
        print("\nMain menu options")
        print("1. Display Balance")
        print("2. Withdrawal")
        print("3. Deposit")
        print("4. Exit")
        try:
            menu_choice = int(input())
        except ValueError:
            print("Enter a valid menu input")
        if 0 < menu_choice < 5:
            if menu_choice == 1:
                display_balance(user_balance)
            elif menu_choice == 2:
                user_balance = display_withdraw(user_balance)
                display_balance(user_balance)
            elif menu_choice == 3:
                 user_balance = display_deposit(user_balance)
                 display_balance(user_balance)
            elif menu_choice == 4:
                display_exit()
            user_reply = input("Would you like to perform another action? (y/n) ")
            if user_reply.lower() == "n":
                display_exit()
        else:
            print("Invalid menu option")
     


def main():
    atm_opener()
    atm_main_menu()


if __name__ == "__main__":
    main()
