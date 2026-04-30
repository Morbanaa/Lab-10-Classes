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
        print(f"Address: {self.address}")
        print(f"Age: {self.age}")
        print(f"Phone: {self.phone_number}")


def main():
    collect_info()



def collect_info():  
    your_name, your_address, your_age, your_phone_number = input("Enter your name, address, age, and phone number with a space between each: ").split()

    friend_name, friend_address, friend_age, friend_phone_number = input("Enter a friends name, address, age, and phone number with a space between each: ").split()

    family_name, family_address, family_age, family_phone_number = input("Enter a family members name, address, age, and phone number with a space between each: ").split()

    your_info = PersonalInfo(your_name,your_address,your_age,your_phone_number)
    friend_info = PersonalInfo(friend_name,friend_address,friend_age,friend_phone_number)
    family_info = PersonalInfo(family_name,family_address,family_age,family_phone_number)

    your_info.display()
    friend_info.display()
    family_info.display()

   

if __name__ == "__main__":
    main()