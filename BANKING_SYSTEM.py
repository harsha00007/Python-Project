import mysql.connector
import random

print("--------------------------")
print("  WELCOME TO HARSHA BANK  ")
print("--------------------------")

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="harsha782002",
    database="bank_system"
)
my_cursor = my_db.cursor()


def my_table():
    my_cursor.execute("create table if not exists bank_table(account_number int, name varchar(200), balance int)")
    my_db.commit()


def create_account(name, initial_deposit):
    account_number = random.randint(10000, 99999)
    my_cursor.execute("INSERT INTO bank_table (account_number, name, balance) VALUES (%s, %s, %s)",
                      (account_number, name, initial_deposit))
    my_db.commit()
    print(f"Account created successfully! and Your Account Number ==> {account_number}\n")


def account_balance(account_number):
    my_cursor.execute("select balance from bank_table where account_number=%s", (account_number,))
    balance = my_cursor.fetchone()
    if balance:
        print()
        print(f"Available balance is {balance[0]}\n")
    else:
        print("Account is not Found\n")


def access_account(user_name, account_number):
    my_cursor.execute("select name, account_number from bank_table where name = %s and account_number = %s",
                      (user_name, account_number))
    data = my_cursor.fetchone()
    if data:
        return True
    else:
        return False


def deposit(deposit_amount, account_number):
    my_cursor.execute("select balance from bank_table where account_number = %s", (account_number,))
    account = my_cursor.fetchone()
    if account:
        balance = account[0]
        new_balance = balance + deposit_amount
        my_cursor.execute("update bank_table set balance= %s where account_number = %s", (new_balance, account_number))
        my_db.commit()
        print(f"Deposit is successful for this account {account_number}")
    else:
        print("Account is not Found")


def withdraw(withdraw_amount, account_number):
    my_cursor.execute("select balance from bank_table where account_number = %s", (account_number,))
    account = my_cursor.fetchone()
    if account:
        balance = account[0]
        if balance >= withdraw_amount:
            new_balance = balance - withdraw_amount
            my_cursor.execute("update bank_table set balance = %s where account_number = %s",
                              (new_balance, account_number))
            my_db.commit()
            print(f"withdraw is successful for this account {account_number}")
        else:
            print("Insufficient balance?")
    else:
        print("Account is not Found")


def delete_account(name, account_number):
    my_cursor.execute("delete from bank_table where name=%s and account_number=%s", (name, account_number))
    my_db.commit()


def all_account_details():
    manager_password = int(input("Enter a password: "))
    if manager_password == 1234:
        print()
        print("Your customer details")
        my_cursor.execute("select * from bank_table")
        my_data = my_cursor.fetchall()
        print("A/c No   Name   Balance\n-----------------------")
        for i in my_data:
            print(i)
        else:
            print()
    else:
        print()
        print("Sorry your not the manager of the this Bank")
        print()


def account_navigation():
    while True:
        print("Enter 1 to Create a new account")
        print("Enter 2 to Access an existing account")
        print("Enter 3 to Delete account")
        print("Enter 4 to All customer data (Only access bank Manager Password Required)")
        print("Enter 5 to Exit\n")
        user_input = input("Enter the number: ")
        if user_input == "1":
            user_name = input("Enter your name: ").lower()
            user_initial_deposit = int(input("Enter a amount: "))
            create_account(user_name, user_initial_deposit)
        elif user_input == "2":
            user_name = input("Enter a user name: ").lower()
            user_account_number = int(input("Enter a account number: "))
            # authenticationStatus = access_account(user_name, user_account_number)
            if access_account(user_name, user_account_number):
                print()
                print(f"This Name: {user_name} and Account Number: {user_account_number} is present in Bank")
                print()
                while True:
                    print("Enter 1 to Withdraw")
                    print("Enter 2 to Deposit")
                    print("Enter 3 to Display Available Balance")
                    print("Enter 4 to Go back to the previous menu")
                    userChoice = input("Enter your choice: ")
                    if userChoice == "1":
                        withdraw_amount = int(input("Enter the Withdraw amount: "))
                        withdraw(withdraw_amount, user_account_number)
                    elif userChoice == "2":
                        deposit_amount = int(input("Enter Deposit amount: "))
                        deposit(deposit_amount, user_account_number)
                    elif userChoice == "3":
                        account_balance(user_account_number)
                    elif userChoice == "4":
                        break
                    else:
                        print("Please enter the correct number")
            else:
                print()
                print(f"This Name: {user_name} and Account Number: {user_account_number} Not in this Bank")
                print()
        elif user_input == "3":
            name = input("Enter a name: ").lower()
            account_number = int(input("Enter account number: "))
            delete_account(name, account_number)
            print("Account deleted successfully")
        elif user_input == "4":
            all_account_details()
        elif user_input == "5":
            break
        else:
            print()
            print("Enter a correct number:")
            print()


my_table()
account_navigation()
my_db.close()
my_cursor.close()


