import csv
from JPCorporateAddressBook import JPCorporateAddressBook
from TestJPCorporateAddressBook import TestJPCorporateAddressBook

test_address_book = TestJPCorporateAddressBook().createAddressBook()

with open('./csv/jigyosyo.csv', 'r', encoding='utf8') as csv_file:

    csv_data = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\n', quotechar='"', skipinitialspace=True)
    csv_list = list(csv_data)

    #print('件数 : {}'.format(len(csv_list)))

    for cnt in range(0,10):

        print('{} : {}'.format(cnt, csv_list[cnt]))
        print('')
        print('企業名 : {}'.format(test_address_book[cnt].name))
        print('住所 : {}'.format(test_address_book[cnt].address))
        print('')

address_book = JPCorporateAddressBook().createAddressBook()

for cnt in range(0,10):

    print('企業名 : {}'.format(address_book[cnt].name))
    print('住所 : {}'.format(address_book[cnt].address))
    print('')
