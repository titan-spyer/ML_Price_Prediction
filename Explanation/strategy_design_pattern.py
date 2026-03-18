from abc import ABC, abstractmethod


# An abstract for payment system.
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        '''Abstract method to pay for a given amount.'''
        pass

class PayPal(PaymentSystem):
    def pay(self, amount):
        '''Pay for a given amount using PayPal.'''
        return f"Paid ${amount} using PayPal."

class CreditCard(PaymentSystem):
    def pay(self, amount):
        '''Pay for a given amount using a credit card.'''
        return f"Paid ${amount} using a credit card."

class BillDesk(PaymentSystem):
    def pay(self, amount):
        '''Pay for a given amount using BillDesk.'''
        return f"Paid ${amount} using BillDesk."


class PaymentContext:
    def __init__(self, strategy: PaymentSystem):
        self.strategy = strategy

    def execute_payment(self, amount):
        return self.strategy.pay(amount)


if __name__ == "__main__":
    # Using PayPal strategy
    paypal_payment = PaymentContext(PayPal())
    print(paypal_payment.execute_payment(100))

    # Using CreditCard strategy
    cc_payment = PaymentContext(CreditCard())
    print(cc_payment.execute_payment(200))

    # Using BillDesk strategy
    billdesk_payment = PaymentContext(BillDesk())
    print(billdesk_payment.execute_payment(300))