class Account:
    def __init__(self,bal,acc):
        self.balance=bal
        self.account_no=acc
        
        
    def debit(self,amount):
        self.balance-=amount
        print("Rs.",amount,"was debited")
        print("total balance=",self.get_balance()) 
        
        
        
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credited")
        print("total balance=",self.get_balance()) 
        
        
    def get_balance(self):
        return self.balance    
                
acc1=Account(100000,45879658325)
acc1.debit(1000)
acc1.credit(120360)
print(acc1.balance) 

