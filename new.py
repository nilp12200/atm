import datetime


class User:
    def __init__(self,user_id,pin):
     self.user_id = user_id
     self.pin = pin
     self.balance = 0
     self.transcation_history = []
     
     
    def get_transcation_histroy(self):
        return self.transcation_history
     
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transcation_history.append((datetime.datetime.now(),"withdraw",amount))
            return True
        else:
         return False
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            self.transcation_history.append((datetime.datetime.now(),"Deposit",amount))
            return True
        else:
         return False
    
    def transfer(self, to_user, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            to_user.balance += amount
            self.transaction_history.append((datetime.datetime.now(), "Transfer to User ID: " + to_user.user_id, amount))
            to_user.transaction_history.append((datetime.datetime.now(), "Transfer from User ID: " + self.user_id, amount))
            return True
        else:
            return False 
     
    
class ATM:
    def __init__(self):
        self.users={}
        
    def authenticate_user(self,user_id,pin):
        if user_id in self.users and self.users[user_id].pin==pin:
            return self.users [user_id]    
        else:
            return None
        
    def add_user(self,user):
        self.users[user.user_id]=user
def main():
    atm=ATM()
    
    neel = User("neel","1234")            
    yash = User("yash","5678")   
    
    atm.add_user(neel)         
    atm.add_user(yash)      
    
    
    while True:
        print("welcome to my atm interface")
        user_id=input(("enter the user id"))   
        pin=input(("enter the pin"))   
        
        user=atm.authenticate_user(user_id,pin)
        
        
        if(user):
            print("autheticate successful")
            while True:
                 print("1. Transcation history")
                 print("2. Withdraw")
               
                 print("3. deposit")
                 print("4. transfer")
                 print("5. quit")
                 
                 choice = input("Enter your choice: ")
                 
                 if choice == "1":
                    print("Transaction History:")
                    for transaction in user.get_transcation_histroy():
                        print(transaction)

                 elif choice == "2":
                    amount = float(input("Enter the amount to withdraw: "))
                    if user.withdraw(amount):
                        print("Withdrawal successful. Your balance is now:", user.balance)
                    else:
                        print("Invalid amount or insufficient balance.")
                 elif choice == "3":
                    amount = float(input("Enter the amount to deposit: "))
                    if user.deposit(amount):
                        print("Deposit successful. Your balance is now:", user.balance)
                        
                    else:
                        print("Invalid amount. Please enter a positive amount.")
                   
                 elif choice == "4":
                    recipient_id = input("Enter the recipient's User ID: ")
                    recipient = atm.authenticate_user(recipient_id, "")
                    if recipient:
                        amount = float(input("Enter the amount to transfer: "))
                        if user.transfer(recipient, amount):
                            print("Transfer successful.")
                        else:
                            print("Invalid amount or insufficient balance.")
                    else:
                        print("Recipient not found.")        


                


                 elif choice == "5":
                    print("Thank you for using the ATM. Goodbye!")
                    exit()

                 else:
                    print("Invalid choice. Please select a valid option.")

        else:
            print("Authentication failed. Please check your User ID and PIN.")


if __name__ == "__main__":
    main()
            
            
    
 
 
    