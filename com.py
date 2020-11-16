class Value:
    def __get__(self, instance, owner):
        if instance.commission < 0:
            print('Cannot be negative!')
        else:
            return int(instance.commission)

    def __set__(self, instance, value):
        if value < 0:
            print('Cannot be negative or zero!')
        else:
            instance.commission = value - instance.commission * value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


new_account = Account(0.1)
new_account.amount = 100
print(new_account.amount)
