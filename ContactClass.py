class Contact(object):

    def __init__(self, FirstName, LastName, PhoneNumber, Email, Location, birth_date):
        self.firstName = FirstName
        self.lastName = LastName
        self.phoneNumber = PhoneNumber
        self.email = Email
        self.location = Location
        self.Bday = birth_date

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getPhoneNumber(self):
        return self.phoneNumber

    def getEmail(self):
        return self.email

    def getLoc(self):
        return self.location

    def setFname(self, Name):
        self.firstName = Name

    def setLname(self, LName):
        self.lastName = LName

    def setPhoneNumber(self, PhoneNumber):
        self.phoneNumber = PhoneNumber

    def setEmail(self, Emaili):
        self.email = Emaili

    def setLocation(self, LocationMe):
        self.location = LocationMe

    def getBirthDate(self):
        return self.Bday

    def setBday(self, BdayNew):
        self.Bday = BdayNew


class contactBook(object):

    def __init__(self):
        self.listi = []
        self.Number_of_contacts = 0

    def __iter__(self):
        for i in self.listi:
            yield i

    def addToList(self, contact):
        self.listi.append(contact)
        self.Number_of_contacts += 1

    def __repr__(self):
        st = ""
        for i in self.listi:
            st += "Name: %s, Last Name: %s, Phone Number = %s, Email = %s, Location = %s, BirthDate = %s\n" % (
                i.getFirstName(), i.getLastName(), i.getPhoneNumber(), i.getEmail(), i.getLoc(), i.getBirthDate())
        return st

    def __getNums__(self):
        return self.Number_of_contacts

    def deleteContact(self, contact):
        if len(self.listi) == 0:
            print("The Contact Book is empty, you cannot delete anything")
            return

        try:
            index = self.listi.index(contact)
            del self.listi[index]
            self.Number_of_contacts -= 1
        except ValueError:
            print("The Contact is not in the list")
            exit(1)

    def __len__(self):
        return len(self.listi)

    def getFullContact(self):
        return self.listi

    def ChangeFirstName(self, contact, newName):
        index = self.listi.index(contact)
        self.listi[index].setFname(newName)

    def ChangeLastName(self, contact, newName):
        index = self.listi.index(contact)
        self.listi[index].setLname(newName)

    def ChangePhoneNumber(self, contact, newName):
        index = self.listi.index(contact)
        self.listi[index].setPhoneNumber(newName)

    def ChangeEmail(self, contact, newName):
        index = self.listi.index(contact)
        self.listi[index].setEmail(newName)

    def ChangeLocation(self, contact, newName):
        index = self.listi.index(contact)
        self.listi[index].setLocation(newName)

    def ChangeBday(self, contact, newName):
        index = self.listi.index(contact)
        self.listi[index].setBday(newName)
