
class Atm_account(object):
    def __init__(self,name,pin,first_name,last_name,balance,transactions,withdraw,deposit):
       self.name=name
       self.pin=pin
       self.first_name=first_name
       self.last_name=last_name
       self.balance=balance
       self.transactions=transactions
       self.withdraw=withdraw or {}
       self.deposit=deposit or {}
    
    def username(self,name):
        print("\033[1;31;40m "+name)
    
    def pin(self,pin):
        print(pin)
        
    def name(self,first_name,last_name):
        print("\033[1;31;40m full nam:-"+first_name+last_name)
    
    def balance(self,balance):
        print(balance)
    
    def transactions(self,transactions):
        print(transactions)
    
    def withdraw(self,withdraw):
        print(withdraw)
    
    def deposit(self,deposit):
        print(deposit)
 

john = Atm_account(
'john',
1243,
'john',
'wick',
12312039012391230,
'''
 transaction in 24 hour:
  1. jio:-1000
  2.amazon prime :-12830
  3.amazon:-56655653
''',
'''
withdraw in 1 week:-
 27.9.21:- 101001
 26.9.21:- 101001
 25.9.21:- 1014565
''',
'''
deposit:-
 1.contact:-14M
 2.contact:-16M
 3.contact:-164M
 4.contact:-154M
 5.contact:-164M
 6.contact:-114M
'''
)

a=  input("enter your name :-")
p = int(input("enter your pin:-"))


# print(john.username())
print(john.name())
print(john.pin())
print(john.balance())
print(john.transactions())
print(john.withdraw())
print(john.deposit())

