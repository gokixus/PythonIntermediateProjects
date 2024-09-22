class PersonContact():
    def __init__(self):
        self.persons = []
        
    def addPerson(self):
        self.name = input("Name: ")
        self.surname = input("Surname: ")
        self.phone = input("Phone No: ")
        self.mail = input("Mail: ")
        
        person = {
            "Name": self.name,
            "Surname": self.surname,
            "Phone No": self.phone,
            "Email": self.mail
        }
        
        self.persons.append(person)
        print(f"{self.name} {self.surname} added to the guide")
        
    def removePerson(self):
        self.name = input("Enter the name of the person you want to delete: ")
        self.surname = input("Enter the surname of the person you want to delete: ")
        
        for person in self.persons:
            if person["Name"] == self.name and person["Surname"] == self.surname:
                self.persons.remove(person)
                print(f"{self.name} {self.surname} was deleted from the guide.\n")
                return
        
        print("The person was not found.\n")
        
    def aboutPerson(self):
        self.name = input("Name: ")
        self.surname = input("Surname: ")

        for person in self.persons:
            if person["Name"] == self.name and person["Surname"] == self.surname:
                print(f"\nName: {person["Name"]}\nSurname: {person["Surname"]}\nTelephone No: {person["Phone No"]}\nEmail: {person["Email"]}\n")
                return
        
        print("The person was not found.\n")
        
    def personList(self):
        if not self.persons:
            print("There is no contact in the directory")
        else:
            for person in self.persons:
                print(f"{person["Name"]} {person["Surname"]}")
            print()
    def menu(self):
        while True:
            print("1- Add Person\n2- Delete Person\n3- About Person\n4- Contact List\n5- Out\n")
            choice = input("Choice: ")
            
            if choice == "1":
                self.addPerson()
            elif choice == "2":
                self.removePerson()
            elif choice == "3":
                self.aboutPerson()
            elif choice == "4":
                self.personList()
            elif choice == "5":
                break
            else:
                print("Invalid transaction. try again\n")
                
contact = PersonContact()
contact.menu()