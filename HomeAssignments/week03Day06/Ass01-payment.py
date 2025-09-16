#payment system - polymorphism

class CreditCardPayment:
    def process_payment(amount):
        return f"Processing credit card payment of {amount}"
    

class  PayPalPayment:
    def process_payment(amount):
        return f"Processing PayPal payment of {amount}"
    

class  BankTransferPayment:
    def process_payment(amount):
        return f"Processing bank transfer of {amount}"
    

def make_payment(payment_method, amount):
    print(payment_method(amount))


if __name__ == "__main__":
    payMethods = ["PayPalPayment","BankTransferPayment","CreditCardPayment"]
    for i in payMethods:
        transac = i()
        i.acc