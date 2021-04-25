# initialise (init)
# login
# register
# generate account number
# bank operations

import random
import datetime
dateNow = datetime.datetime.now()

database = {
    4358227722 : [ "Mac", "Henry", "MacHenry@gmail.com", "password", 500]
}


def init():
    print("welcome to Mackies Bank")
    have_account = int(input("Do you have an account with us? 1 (yes) 2 (no):\n "))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("invalid option, please select a valid option")
        init()


def login():
    print("*****login here*****")
    user_account_number = int(input("What is your account number? \n"))
    user_password = input("What is your password \n")

    for account_number, user_details in database.items():
        if account_number == user_account_number:
            if user_details[3] == user_password:
                bank_operations(user_details)
            else:
                print("Invalid account number or wrong password")
                login()


def register():
    print("register here")
    global first_name
    first_name = input("What is your first name? \n")
    global last_name
    last_name = input("What is your last name? \n")
    email = input("What is your email address? \n")
    password = input("create a strong password \n")
    global balance
    balance = 0
    account_number = generate_account_number()
    print("This is your account number: %d" % account_number)

    database[account_number] = [first_name, last_name, email, password, balance]
    print("Account creation successful")
    login()

def bank_operations(user):
    print("Hello %s %s welcome to Mackies Bank" % (user[0], user[1]))
    print("Login Date/Time: %s" % dateNow)
    print("These are the option available")
    print("1. Withdrawal")
    print("2. Cash Deposit")
    print("3. Complaint")
    print("4. Exit")
    print("5. Logout")

    selected_option = int(input("What bank operation would you like to perform? \n"))
    if selected_option == 1:
        withdraw(user)
    elif selected_option == 2:
        deposit(user)
    elif selected_option == 3:
        complaints(user)
    elif selected_option == 4:
        exit()
    elif selected_option == 5:
        logout()
    else:
        print("Invalid option, please try again")

def withdraw(user):
    print("Your current account balance is %d" % user[4])
    withdrawal = int(input("How much would you like to withdraw? \n"))
    if withdrawal > user[4]:
        print("You do not have enough money in your account")
        withdraw(user)
    elif withdrawal < user[4]:
        new_balance = withdrawal - user[4]
        print("current balance is %d" % new_balance)
        menu(user)
    else:
        print("Invalid details")
        withdraw(user)

def deposit(user):
    print("deposit cash")
    deposit_amount = int(input("How much would you like to deposit? \n"))
    deposited = user[4] + deposit_amount
    print("Current balance: ₦%s" % deposited)
    menu(user)


def complaints(user):
    input("What issue would you like to report? \n")
    print("Thank you for contacting us")
    menu(user)

def menu(user):
    selected_option = int(input("Would you like to perform another bank operation? 1(withdraw), 2(deposit), 3(compliants), 4(exit), 5(logout) \n"))
    if selected_option == 1:
        withdraw(user)
    elif selected_option == 2:
        deposit(user)
    elif selected_option == 3:
        complaints(user)
    elif selected_option == 4:
        exit()
    elif selected_option == 5:
        logout()
    else:
        print("Invalid option, please try again")

def exit():
    login()

def logout():
    init()

def generate_account_number():
    return random.randrange(1111111111, 9999999999)

init()