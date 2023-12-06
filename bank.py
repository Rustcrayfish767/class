#for ref Sun Nov 19 20:25:14 2023,John Smith,johns,ufxxbtwi,100,1000,deposit

import encrypt
import sys
import csv
from datetime import datetime
current_time = datetime.now()
formatted = current_time.strftime("%m-%d %H:%M:%S %Y")
def file_reader(user):
    try:
        with open(f'{user}', "r") as data:
            read = csv.reader(data)
            # goes through the rows to get the fourth element of each row 
            for row in read:
                password_1 = row[3]
                realname = row[1]
                return password_1,realname
                
                
        
    except Exception as e:
        print(f"Something went wrong. Please enter a valid account.\nError type: {e}")
        main()
        


def login(user,realname,encypted_password):
    print(f"Welcome back {realname}")
    while True:
        try:
            x = int(input("""\n\nWhat would you like to do today?
1. Check balance
2. Deposit into checkings
3. Withdraw from checkings
4. Deposit into savings
5. Withdraw from savings
6. Exit
Enter the number of what you want to do: """))

            if x == 1:
                check_balance(user, realname, encypted_password)
            elif x == 2:
                deposit_checkings(user, realname, encypted_password)
            elif x == 3:
                withdraw_checkings(user, realname, encypted_password)
            elif x == 4:
                deposit_savings(user, realname, encypted_password)
            elif x == 5:
                withdraw_savings(user, realname, encypted_password)
            elif x == 6:
                print("Exiting. Have a great day!")
                sys.exit()
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")

 
def check_balance(user,realname,encypted_password):
    print("Checking balance...")  
    with open(f'{user}', "r") as data:
        read = csv.reader(data)
        for row in read:
            checking = row[4]
            savings = row[5]
    print(f"you have {checking} in your checkings and {savings} in your savings\n\n")
    login(user,realname,encypted_password)




def deposit_checkings(user, realname, encrypted_password):
    with open(user) as file:
        lines = file.readlines()

        last_line = lines[-1].strip()
        read = last_line.split(',')

        checking = float(read[4])
        savings = float(read[5])

    print(f"You have {checking} checkings.")
    amount = float(input("Please enter the amount you wish to deposit into checkings: "))
    print(f"Amount entered: {amount}")
    new_tot = checking + amount



    with open(user, "a", newline="") as data:
        data.write(f"{formatted},{realname},{user},{encrypted_password},{new_tot:.2f},{savings:.2f},deposit\n")

    login(user, realname, encrypted_password)
def deposit_savings(user, realname, encrypted_password):
    with open(user) as file:
        lines = file.readlines()

        last_line = lines[-1].strip()
        read = last_line.split(',')

        checking = float(read[4])
        savings = float(read[5])

    print(f"You have {savings} savings.")
    amount = float(input("Please enter the amount you wish to deposit into savings: "))
    print(f"Amount entered: {amount}")
    new_tot = savings + amount
    with open(user, "a", newline="") as data:
        data.write(f"{formatted},{realname},{user},{encrypted_password},{checking:.2f},{new_tot:.2f},deposit\n")



def withdraw_checkings(user,realname,encypted_password):
    with open(user) as file:
        lines = file.readlines()

        last_line = lines[-1].strip()
        read = last_line.split(',')

        checking = float(read[4])
        savings = float(read[5])

    print(f"You have {checking} checkings.")
    amount = float(input("Please enter the amount you wish to withdraw from checkings: "))
    print(f"Amount entered: {amount}")
    if amount > checking:
        print("sorry the amount entered is greater then the current account balance please try agine")
        login(user, realname, encypted_password)

    new_tot = checking - amount



    with open(user, "a", newline="") as data:
        data.write(f"{formatted},{realname},{user},{encypted_password},{new_tot:.2f},{savings:.2f},withdraw\n")

    login(user, realname, encypted_password)
def withdraw_savings(user, realname, encrypted_password):
    with open(user) as file:
        lines = file.readlines()

        last_line = lines[-1].strip()
        read = last_line.split(',')

        checking = float(read[4])
        savings = float(read[5])

    print(f"You have {savings} savings.")
    amount = float(input("Please enter the amount you wish to deposit into savings: "))
    print(f"Amount entered: {amount}")
    if amount > savings:
        print("sorry the amount entered is greater then the current account balance please enter a valid number")
        login(user, realname, encrypted_password)
    new_tot = savings - amount
    with open(user, "a", newline="") as data:
        data.write(f"{formatted},{realname},{user},{encrypted_password},{checking:.2f},{new_tot:.2f},deposit\n")
    login(user, realname, encrypted_password)

def main():
    
    #print(formmated)

    user = input("Please enter your username: ")
    password_1,realname = file_reader(user)
    enterpass = input("Please enter your password: ")   
    encrypted_password = encrypt.encrypt(enterpass)
    #print(f"debug",encrypted_password)
    #print(f"DEBUG file password{password_1}")
    if encrypted_password == password_1:
        login(user,realname,encrypted_password) 
    elif encrypted_password != password_1:
        print("sorry that password is incorect please try again")
        main()
    


if __name__ == "__main__":
    main()
