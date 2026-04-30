# Teddy Rodd
# Lab 10 
#Personal Information Class

class PersonalInfo():
    def __init__(self,name,address,age,phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number

    def display(self):
        print("-------------------------")
        print("           Data:")
        print("-------------------------")
        print(f"Name: {self.name}")
        print(f"Address: {self.name}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone_number}")


