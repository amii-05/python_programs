#ABSTRACTION

# abstraction - hiding the internal details and showing only essential features

from abc import ABC,abstractmethod
class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(Payment):
    def pay(self):
        print("Payment completed using upi")
class GPay(Payment):
    def pay(self):
        print("Payment completed using gpay")
class Phonepe(Payment):
    def pay(self):
        print("Payment completed using phonepe")
payment=UPI()
payment.pay()
payment=GPay()
payment.pay()
payment=Phonepe()
payment.pay()
