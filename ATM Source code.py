#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Atm:
    def __init__(self):
        self.pin = " "
        self.balance = 0

        
        self.menu()
    def  menu(self):
            user_input = input("""
            hell, how would you like to proceed?
            1.enter 1 to create pin
            2.enter 2 to deposite
            3.enter 3 to withdraw
            4.enter 4 to check balance
            5.enter 5 to exit
        """)
            if user_input == "1":
                self.create_pin()
                print("create pin")
            elif user_input == "2":
                self.deposite()
                print("deposite")
            elif user_input == "3":
                self.withdraw()
                print("withdraw")
            elif user_input == "4":
                self.check_balance()
                print("check balance")
            else:
                print("bye")
    def create_pin(self):
        self.pin = input("enter your pin")
        print("pin set succesfully")
        
    def deposite(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            self.balance = self.balance + amount
            print("deposite succesfully")
            
        else :
            print("invalid")
            
    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            if amount < self.balance:
                self.balance = self.balance-amount
                print("operation succesful")
        
            else:
                print("insufficient funds")
                
                
        else:
            print("invalid pin")
            
            
    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.pin:
            print(self.balance)
            
        else:
        
            print("invalid pin")
            
                


# In[2]:


sbi = Atm()


# In[3]:


sbi.deposite()


# In[4]:


sbi.check_balance()


# In[5]:


sbi.withdraw()


# In[6]:


sbi.check_balance()


# In[ ]:




