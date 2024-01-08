class BankAccount:
    id: int = None
    bank_id: int = None
    user_id: int = None
    amount: int = None
    currency: int = None

    def __init__(self, id: int, bank_id: int, user_id: int, 
                  amount: int, currency: int):
        self.id = id
        self.bank_id = bank_id
        self.user_id = user_id
        self.amount = amount
        self.currency = currency

    def money_transfer(self, id_from: int, id_to: int, amount):
        pass