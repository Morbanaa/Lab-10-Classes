# Teddy Rodd
# Lab 10 
# Personal Information Class

class PersonalInfo():
    def __init__(self,name,address,age,phone_number):
        self.name = name
        self.address = address
        self.age = age
        self.phone_number = phone_number
    
    # Accessors AKA Getters
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone_number(self):
        return self.phone_number


    # Mutators AKA Setters
    def set_name(self,name):
        self.name = name

    def set_address(self,address):
        self.address = address

    def set_age(self,age):
        self.age = age

    def set_phone(self,phone_number):
        self.phone_number = phone_number

    def display(self):
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone_number}")
        print()


def main():
    your_info = PersonalInfo("None", "408 FakeStreet", "18","9999999999")
    friend_info = PersonalInfo("None", "408 FakeStreet", "18","9999999999")
    family_info = PersonalInfo("None", "408 FakeStreet", "18", "9999999999")

    #Changes using Setters
    your_info.set_name("Teddy")
    your_info.set_address("408 West Jefferson")
    your_info.set_age("26")
    your_info.set_phone("9707491263")

    friend_info.set_name("Sora")
    friend_info.set_address("4090 Forever Circle")
    friend_info.set_age("12")
    friend_info.set_phone("6302473456")

    family_info.set_name("Heather")
    family_info.set_address("123 Oak Drive")
    family_info.set_age("33")
    family_info.set_phone("8603245467")


    print("-------------------------")
    print("           Data:")
    print("-------------------------")
    your_info.display()
    friend_info.display()
    family_info.display()

    # Example using my getters
    print("\nJust Names List:")
    print(your_info.get_name())
    print(friend_info.get_name())
    print(family_info.get_name())


if __name__ == "__main__":
    main()



"""
Output:

-------------------------
           Data:
-------------------------
Name: Teddy
Address: 408 West Jefferson
Age: 26
Phone: 9707491263

Name: Sora
Address: 4090 Forever Circle
Age: 12
Phone: 6302473456

Name: Heather
Address: 123 Oak Drive
Age: 33
Phone: 8603245467


Just Names List:
Teddy
Sora
Heather
Press any key to continue . . .


"""