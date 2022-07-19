from JPCorporateAddressBook import JPCorporateAddressBook

if __name__ == '__main__':

    address_book = JPCorporateAddressBook().createAddressBook()

    for page in address_book:

        print('企業名 : {}'.format(page.name))
        print('住所 : {}'.format(page.address))
        print('')
