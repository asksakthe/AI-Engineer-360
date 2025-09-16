#payment system - polymorphism

class CreditCardPayment:
    def process_payment(self,amount):
        self.amount = amount
        return f"Processing credit card payment of {self.amount}"
    

class  PayPalPayment:
    def process_payment(self,amount):
        self.amount = amount
        return f"Processing PayPal payment of {self.amount}"
    

class  BankTransferPayment:
    def process_payment(self,amount):
        self.amount = amount
        return f"Processing bank transfer of {self.amount}"
    

# ui = BankTransferPayment()
# print(ui.process_payment(900))
def make_payment(payment_method, amount):
    transac = payment_method()
    return transac.process_payment(amount)
    #print(payment_method(amount))


if __name__ == "__main__":
    payMethods = [PayPalPayment,BankTransferPayment,CreditCardPayment]
    for i in payMethods:
        print(i.__name__)
        call_func = make_payment(i, 500)
        print(call_func)

        