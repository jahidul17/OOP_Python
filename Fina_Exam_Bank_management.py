
import random

# -----------------------------------------
class Bank:
    def __init__(self,name,initial_amount) -> None:
        self.name=name
        self.__userList=[]
        self.__adminList=[]
        self.balance=initial_amount
        self.total_Loan=0
        self.loan=True
        self.bankrupt=True

    def create_user_account(self,user):
        self.__userList.append(user)
        print("User account created successfully!")

    def create_admin_account(self,admin):
        self.__adminList.append(admin)
        print("Admin account created successfully!")

    def delete_account(self,email):
        for useraccount in self.__userList:
            if email==useraccount.email:
                self.__userList.remove(useraccount)
                print("User account deleted successfully!")
            else:
                print("User not found!")

    def transfer_amount(self,send_mail,receive_mail,amount):
        sender=self.find_user(send_mail)
        receiver=self.find_user(receive_mail)
        
        if sender is not None:
            if receiver is not None:
                if sender.balance>amount:
                    sender.balance -= amount
                    receiver.balance += amount
                    print(f"From {send_mail}")
                    print(f"To {receive_mail}")
                    print(f"{amount} tk Send Successfully!")
                else:
                    print("Your account have not sufficient balance.")
            else:
                print("Receiver account is not valid.")
        else:
            print("Sender account is not valid.")



    def all_user_list(self):
        for user_ac in self.__userList:
            print(f"User Name: {user_ac.name} \t User Email: {user_ac.email} \t User Adress: {user_ac.address}")


    def all_admin_list(self):
        for admin_ac in self.__adminList:
            print(f"Admin Name: {admin_ac.name} \t Admin Email: {admin_ac.email}")

    def loan_amount(self):
        print(f"Total bank loan: {self.total_Loan} tk only")

    def bank_amount(self):
        print(f"Total Bank amount: {self.balance} tk only")

    def find_user(self,email):
        for user_ac in self.__userList:
            if email==user_ac.email:
                return user_ac
        return None
    
    def find_admin(self,email):
        for admin_ac in self.__adminList:
            if email==admin_ac.email:
                return True
        return False
    
    def find_email(self,email):
        for us_acc in self.__userList:
            if email==us_acc.email:
                return True
        return False

    def loan_status(self,signal):        
        if signal=="on":
            self.loan=True
            print("Loan status on.")
        elif signal=="off":
            self.loan=False
            print(f"Loan status off")
        else:
            print("Invalid Input!")


    def bankrupt_status(self,signal):
        if signal=="off":
            self.bankrupt=True
            print("Bankrupt status off.")
        elif signal=="on":
            self.bankrupt=False
            print(f"Bankrupt status on")
        else:
            print("Invalid Input!")

# ---------------------------------------------
class User:
    def __init__(self,name,email,address) -> None:
        self.name=name
        self.email=email
        self.address=address

class Client(User):
    def __init__(self, name, email, address,account_type) -> None:
        super().__init__(name, email, address)
        self.account_type=account_type
        self.balance=0
        self.__transactionHistory=[]
        self.__loan_tk=0
        self.__accountNo=random.randint(1001,2999)

    def history(self):
        print("--------Your Transaction History--------")
        for histo in self.__transactionHistory:
            for key, value in histo.items():
                print(f"{key}: {value}")
            print("\n")


    def deposit(self,amount,bank):
        self.balance += amount
        bank.balance += amount
        print(f"Deposit {amount} tk is successful!")
        self.__transactionHistory.append({"Operation": "Deposit", "Amount": amount})

    def withdraw(self,amount,bank):
        if bank.bankrupt:
            if self.balance>=amount:
                self.balance -= amount
                bank.balance -= amount
                self.__transactionHistory.append({"Operation": "Withdraw","Amount": amount})

            else:
                print("Withdrawal amount exceeded")
        else:
            print("-----Sorry!!!-------")
            print("The bank is bankrupt")
    

    def check_amount(self):
        print(f"Now, Your Balance : {self.balance}")


    def take_loan(self,amount,bank):
        max_time=1
        if bank.loan:
            if max_time<=2:
                if bank.balance>amount:
                    self.__loan_tk += amount
                    bank.total_Loan += amount
                    print(f"Thanks! Yout got loan {amount} tk.")
                    max_time+=1
                else:
                    print("Sorry!!! Currently bank have no money")
            else:
                print("Sorry! Loan limit exceded")
        else:
            print("Sorry!!! Loan status is off.")
    
    def loan_amount(self):
        print(f"You have loan {self.__loan_tk} tk")

    
    def send_money(self,receive_mail,amount,bank):
        bank.transfer_amount(self.email,receive_mail,amount)
        self.__transactionHistory.append({"Operation": "Send Money","To": receive_mail,"Amount": amount})


# ----------------------------------------------------------------

class Admin(User):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)

    def create_admin_account(self,adminInfo,bank):
        bank.create_admin_account(adminInfo)

    def delete_any_user_account(self,email,bank):
        bank.delete_account(email)

    def see_all_user_account(self,bank):
        bank.all_user_list()

    def see_all_admin_account(self,bank):
        bank.all_admin_list()

    def check_total_available_balance(self,bank):
        bank.bank_amount()

    def check_total_loan_amount(self,bank):
        bank.loan_amount()

    def loan_status(self,signal,bank):
        bank.loan_status(signal)

    def bankrupt_status(self,signal,bank):
        bank.bankrupt_status(signal)

# ------------------------------------------------------

default_bank=Bank("Al-Arafah Islami Bank PLC",0)
owner=Admin("Zahidul Islam","zahidul@gmail.com","Patuakhali")
owner.create_admin_account(owner,default_bank)

# --------------------------------------------------------

def user_menu(demo_user):
    while True:
        print("----------Access menu as a user----------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Take Loan")
        print("5. Check Loan")
        print("6. Send Money")
        print("7. History")
        print("8. Exit")
    
        choice=int(input("Enter your choice whith in 1 to 8: "))

        if choice==1:
            amount=int(input("Enter deposit amount: "))
            demo_user.deposit(amount,default_bank)
        elif choice==2:
            amount=int(input("Enter withdraw amount: "))
            demo_user.withdraw(amount,default_bank)
        elif choice==3:
            demo_user.check_amount()
        elif choice==4:
            amount=int(input("Enter loan amount: "))
            demo_user.take_loan(amount,default_bank)
        elif choice==5:
            demo_user.loan_amount()
        elif choice==6:
            receiver_mail=input("Enter receiver email: ")
            send_tk=int(input("Enter amount: "))
            demo_user.send_money(receiver_mail,send_tk,default_bank)
        elif choice==7:
            demo_user.history()
        elif choice==8:
            break
        else:
            print("Invalid Input")


def admin_menu():
    while True:
        print("----------Access menu as a admin----------")
        print("1. Create a admin account")
        print("2. Delete any user account")
        print("3. See all user account")
        print("4. See all admin account")
        print("5. Check available balance of the Bank")
        print("6. Check total loan of the Bank")
        print("7. Loan feature 'on'/'off' ")
        print("8. Bankrupt feature 'on'/'off' ")
        print("9. Exit")

        choice=int(input("Write choice: "))
        if choice==1:        
            ad_name=input("Enter your Name: ")        
            ad_email=input("Enter your Email: ")        
            ad_adress=input("Enter your Address: ")
            admin_info=Admin(ad_name,ad_email,ad_adress)
            owner.create_admin_account(admin_info,default_bank)
        elif choice==2:        
            us_email=input("Enter user email: ")
            owner.delete_any_user_account(us_email,default_bank)
        elif choice==3:
            owner.see_all_user_account(default_bank)
        elif choice==4:
            owner.see_all_admin_account(default_bank)
        elif choice==5:
            owner.check_total_available_balance(default_bank)
        elif choice==6:
            owner.check_total_loan_amount(default_bank)
        elif choice==7:
            print("Please enter 'on'/'off' for loan status.")
            signal=input("Write Here: ")
            owner.loan_status(signal,default_bank)
        elif choice==8:
            print("Please enter 'on'/'off' for bankrupt status.")
            signal=input("Write Here: ")
            owner.bankrupt_status(signal,default_bank)
        elif choice==9:
            break
        else:
            print("Invalid Input!")


# ---------------------------------------------------------

def admin_login():        
    print("Default admin email: 'zahidul@gmail.com' ")
    email=input("Enter your admin email: ")
    if default_bank.find_admin(email):
        admin_menu()
    else:
        print("Admin email not found.")


def user_login():
    while True:
        print("1. User login")
        print("2. Create a account")
        print("3. Exit")
        choice=int(input("Enter choice within 1 to 3: "))

        if choice==1:
            email=input("Enter your email: ")
            if default_bank.find_user(email) is not None:
                user_menu(default_bank.find_user(email))
            else:
                print("Your email is not found.")
                print("Please try again or create a new account.")
        elif choice==2:
            us_name=input("Enter your name: ")
            us_email=input("Enter your email: ")
            us_adress=input("Enter your adress: ")
            us_acc_type=input("Enter account type 'Savings' or 'Cuurent' : ")

            if default_bank.find_email(us_email):
                print("Already Exist")
            else:
                demo_user=Client(us_name,us_email,us_adress,us_acc_type)
                default_bank.create_user_account(demo_user)
                user_menu(demo_user)
        elif choice==3:
            break
        else:
            print("Invalid Input")
            

# -------------------------------------------------------

while True:
    print("--------Wellcome--------")
    print("1. Customer panel ")
    print("2. Admin panel ")
    print("3. Exit ")

    choice=int(input("Enter your option within 1 to 3: "))

    if choice==1:
        user_login()
    elif choice==2:
        admin_login()
    elif choice==3:
        break
    else:
        print("Invalid Input")



# ----------------------------The_End--------------------------------