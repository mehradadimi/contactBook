import datetime


from ContactClass import *


def main():
    """Create Contact Book"""

    contactBook1 = contactBook()

    """ Creating Contact Numbers"""

    Bday_contact1 = datetime.datetime(2000, 1, 12, 12, 34, 54)
    Bday_contact2 = datetime.datetime(2005, 1, 5, 8, 32, 12)
    Bday_contact3 = datetime.datetime(1997, 1, 1, 3, 12, 9)

    contact1 = Contact('Ali', 'Hajipoor', "0912-144-5566", 'Ali.hj@gmail.com', 'Sari', Bday_contact1)
    contact2 = Contact('Sam', 'Nab', "0911-111-1111", 'Sam.nab@gmail.com', 'Tehran', Bday_contact2)
    contact3 = Contact('Hossein', 'Alavi', "0913-141-1617", 'Hossein.al@yahoo.com', 'Mashhad', Bday_contact3)

    """Adding the Contacts to the list"""

    contactBook1.addToList(contact1)
    contactBook1.addToList(contact2)
    contactBook1.addToList(contact3)

    """Printing the list"""

    print(contactBook1)
    print("There are %d contacts in this book\n" % len(contactBook1))

    """Deleting A contact twice"""

    contactBook1.deleteContact(contact1)
    print(contactBook1)
    print(len(contactBook1))

    contactBook1.deleteContact(contact1)
    print(contactBook1)
    print(len(contactBook1))

    """Deleting Contacts one by one"""

    contactBook1.deleteContact(contact1)
    print(contactBook1)
    print(len(contactBook1))

    contactBook1.deleteContact(contact2)
    print(contactBook1)
    print(len(contactBook1))
    #
    contactBook1.deleteContact(contact3)
    print(contactBook1)
    print(len(contactBook1))

    """Changing the Contact Using Contact Class"""

    contact1.setFname("Mehrad")
    print(contactBook1)
    #
    contact2.setEmail("Mehrad@gmail.com")
    print(contactBook1)

    """Changing the Contact Using ContactBook Class"""

    contactBook1.ChangeFirstName(contact1, 'Alireza')
    print(contactBook1)
    #
    contactBook1.ChangeLastName(contact2, 'Shah Moradi')
    print(contactBook1)


if __name__ == '__main__':
    main()
