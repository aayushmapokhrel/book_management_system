
class UserService:
    def add_balance(userbalance,amount):
        previous_amount = userbalance.balance
        balance = previous_amount + amount
        userbalance.balance = balance
        userbalance.save()
        return userbalance