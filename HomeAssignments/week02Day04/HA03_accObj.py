import HA03_BankAcc as bk
#create object of BankAccount Class
acc_obj_01 = bk.BankAccount('Sakthi', 15000, 'Savings')
print(acc_obj_01.display_balance(5000))
print(acc_obj_01.deposit(2000))
#withdraw amount 
acc_obj_01.Withdraw(1000)
print("#########################################################")
#sceanrio 2 - insufficient balance check
acc_obj_02 = bk.BankAccount('Karthi', 10000, 'Current')
print(acc_obj_02.display_balance(10000))
print(acc_obj_02.deposit(5000))
#withdraw amount more than balance
acc_obj_02.Withdraw(20000)
print("#########################################################")
acc_obj_02.Withdraw(5000)
#print("#########################################################")
print(acc_obj_02.display_balance(15000))

