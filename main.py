import BankAccount 
import Bank
import User



Alfa = Bank.Bank(id = 0, name = "Alfa")
print(Alfa.id, " ", Alfa.name)
assert Alfa.id == 0 and Alfa.name == "Alfa"

Anton_user = User.User(id = 0, first_name = "Anton", last_name = "Kovalevich", 
                       email = "@mail.com", password = "123")

copy_for_debag = Anton_user

#создать фукцию открытия счета, депозит и кредит (в файле банк аккаунт, основной класс будет родительским)