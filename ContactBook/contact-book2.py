class PersonContact():
    def __init__(self, fileName = "contact1.txt"):
        self.persons = []
        self.fileName = fileName
        
    def addPerson(self):
        name, surname = input("Name and Surname: ").split()
        phone = input("Phone No: ")
        mail = input("Mail: ")
        
        person = {
            "name": name,
            "surname": surname,
            "phone": phone,
            "mail": mail
        }
        self.persons.append(person)
        print(f"{name} {surname} added to the guide.\n")
        self.saveFile(person)
        
    def removePerson(self):
        name, surname = input("Enter the name and surname of the person you want to delete: ").split()

        for person in self.persons:
            if person["name"] == name and person["surname"] == surname:
                self.persons.remove(person)
                print(f"{name} {surname} was deleted from the guide.\n")
                self.rewriteFile()
                return

        print("The person was not found.\n")
        
    def about_person(self):
        name, surname = input("Name and surname: ").split()
        
        for person in self.persons:
            if person["name"] == name and person["surname"] == surname:
                print(f"\nName: {person["name"]}\nSurname: {person["surname"]}\nPhone No: {person["phone"]}\nMail: {person["mail"]}\n")
                return

        print("The person was not found.\n")
        
    def person_list(self):
        if not self.persons:
            print("There is no contact in the directory")
        else:
            print("\n-------Contacts-------")
            for person in self.persons:
                print(f"{person["name"]} {person["surname"]}")
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
                self.about_person()
            elif choice == "4":
                self.person_list()
            elif choice == "5":
                break
            else:
                print("Invalid transaction. try again\n")
        
    def loadFile(self):
        try:
            with open(self.fileName, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    if len(parts) == 3:
                        nameSurname = parts[0]
                        phone = parts[1].split(": ")[1]
                        mail = parts[2].split(": ")[1]
                        name, surname = nameSurname.split()
                        person = {
                            "name": name,
                            "surname": surname,
                            "phone": phone,
                            "mail": mail
                        }   
                        self.persons.append(person)
                    else:
                        print(f"Invalid line format: {line}")
        except FileNotFoundError:
            print("File not found. Starting with an empty contact list.")
            
    def saveFile(self, person):
        with open(self.fileName, "a", encoding="utf-8") as file:
            file.write(f"{person["name"]} {person["surname"]}, Phone: {person["phone"]}, Mail: {person["mail"]}\n")
            
    def rewriteFile(self):
        with open(self.fileName, "w", encoding="utf-8") as file:
            for person in self.persons:
                file.write(f"{person["name"]} {person["surname"]}, Phone: {person["phone"]}, Mail: {person["mail"]}\n")
contact = PersonContact()
contact.loadFile()
contact.menu()