import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox

class PersonContact(QWidget):
    def __init__(self, fileName="contact2.txt"):
        super().__init__()
        self.persons = []
        self.fileName = fileName
        self.initUI()
        self.loadFile()

    def initUI(self):
        self.setWindowTitle("Contact Manager")
        
        # Layout
        self.layout = QVBoxLayout()

        # Name and Surname Input
        self.nameLabel = QLabel("Name:")
        self.layout.addWidget(self.nameLabel)
        self.nameInput = QLineEdit()
        self.layout.addWidget(self.nameInput)

        self.surnameLabel = QLabel("Surname:")
        self.layout.addWidget(self.surnameLabel)
        self.surnameInput = QLineEdit()
        self.layout.addWidget(self.surnameInput)

        # Phone and Email Input
        self.phoneLabel = QLabel("Phone No:")
        self.layout.addWidget(self.phoneLabel)
        self.phoneInput = QLineEdit()
        self.layout.addWidget(self.phoneInput)

        self.emailLabel = QLabel("Mail:")
        self.layout.addWidget(self.emailLabel)
        self.emailInput = QLineEdit()
        self.layout.addWidget(self.emailInput)

        # Buttons
        self.addButton = QPushButton("Add Person")
        self.addButton.clicked.connect(self.addPerson)
        self.layout.addWidget(self.addButton)

        self.deleteButton = QPushButton("Delete Person")
        self.deleteButton.clicked.connect(self.removePerson)
        self.layout.addWidget(self.deleteButton)
        
        self.aboutButton = QPushButton("About")
        self.aboutButton.clicked.connect(self.aboutPerson)
        self.layout.addWidget(self.aboutButton)

        self.listButton = QPushButton("Show Contacts")
        self.listButton.clicked.connect(self.person_list)
        self.layout.addWidget(self.listButton)

        self.resultArea = QTextEdit()
        self.resultArea.setReadOnly(True)
        self.layout.addWidget(self.resultArea)

        self.setLayout(self.layout)

    def addPerson(self):
        self.resultArea.clear()
        
        name = self.nameInput.text()
        surname = self.surnameInput.text()
        phone = self.phoneInput.text()
        mail = self.emailInput.text()

        if not name or not surname or not phone or not mail:
            QMessageBox.warning(self, "Input Error", "Please fill all fields!")
            return

        person = {
            "name": name,
            "surname": surname,
            "phone": phone,
            "mail": mail
        }
        self.persons.append(person)
        self.resultArea.append(f"{name} {surname} added to the guide.\n")
        
        self.saveFile(person)
        
        self.nameInput.clear()
        self.surnameInput.clear()
        self.phoneInput.clear()
        self.emailInput.clear()

    def removePerson(self):
        self.resultArea.clear()
        name = self.nameInput.text()
        surname = self.surnameInput.text()

        for person in self.persons:
            if person["name"] == name and person["surname"] == surname:
                self.persons.remove(person)
                self.resultArea.append(f"{name} {surname} was deleted from the guide.\n")
                self.rewriteFile()
                return

        QMessageBox.warning(self, "Error", "The person was not found.")
        
    def aboutPerson(self):
        name = self.nameInput.text()
        surname = self.surnameInput.text()

        for person in self.persons:
            if person["name"] == name and person["surname"] == surname:
                self.resultArea.clear()
                self.resultArea.append(f"Name: {person['name']}")
                self.resultArea.append(f"Surname: {person['surname']}")
                self.resultArea.append(f"Phone: {person['phone']}")
                self.resultArea.append(f"Mail: {person['mail']}")
                return
        
        self.resultArea.clear()
        self.resultArea.append("The person was not found.\n")
        
    def person_list(self):
        self.resultArea.clear()
        if not self.persons:
            self.resultArea.append("There is no contact in the directory.\n")
        else:
            self.resultArea.append("-------Contacts-------\n")
            for person in self.persons:
                self.resultArea.append(f"{person["name"]} {person["surname"]}")
                

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
        except FileNotFoundError:
            self.resultArea.append("File not found. Starting with an empty contact list.\n")

    def saveFile(self, person):
        with open(self.fileName, "a", encoding="utf-8") as file:
            file.write(f"{person["name"]} {person["surname"]}, Phone: {person["phone"]}, Mail: {person["mail"]}\n")

    def rewriteFile(self):
        with open(self.fileName, "w", encoding="utf-8") as file:
            for person in self.persons:
                file.write(f"{person["name"]} {person["surname"]}, Phone: {person["phone"]}, Mail: {person["mail"]}\n")
                
app = QApplication(sys.argv)
win = PersonContact()
win.show()
sys.exit(app.exec_())
