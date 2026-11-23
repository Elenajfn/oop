# Problem 1
class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"


# Problem 2
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old, I live at {self.address}."


class Student(Person):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)
        self.field_of_study = field_of_study

    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old, and I study {self.field_of_study}."


class Employee(Person):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old, and I work at {self.company}."


# Problem 3
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def transfer(self, destination, amount):
        # False if not enough money, True if the transfer worked
        if not self.withdraw(amount):
            return False
        destination.deposit(amount)
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.0):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def check_balance(self):
        return self.balance


if __name__ == "__main__":
    print(Vehicle().drive(), "|", Car().drive(), "|", Bicycle().drive())
    print(Student("Ana", 20, "Paris", "Math").introduce())
    print(Employee("Bob", 40, "Lyon", "Google").introduce())
    a = SavingsAccount("A1", 100, 0.1)
    b = BankAccount("B1", 50)
    print(a.transfer(b, 30), a.balance, b.balance)
    print(a.transfer(b, 500))
    a.add_interest()
    print(a.check_balance())
