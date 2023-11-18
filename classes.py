class Employee:
    def __init__(self, name, email, pay):
        self.name = name
        self.email = email
        self.pay = pay

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_pay(self):
        return self.pay

    def set_name(self, new_name):
        self.name = new_name

    def set_email(self, new_email):
        self.email = new_email

    def set_pay(self, new_pay):
        self.pay = new_pay

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Pay: ${self.pay} per hour")

    def give_raise(self, amount):
        self.pay += amount
        print(f"{self.name} received a raise of ${amount}. New pay: ${self.pay} per hour")

employee1 = Employee("John Doe", "john@example.com", 20.0)

employee1.display_info()

employee1.give_raise(2.0)

employee1.display_info()
