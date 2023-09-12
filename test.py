import csv
from JPCorporateAddressBook import JPCorporateAddressBook
from TestJPCorporateAddressBook import TestJPCorporateAddressBook

test_address_book = TestJPCorporateAddressBook().createAddressBook()
address_book = JPCorporateAddressBook().createAddressBook()

with open('./csv/jigyosyo.csv', 'r', encoding='utf8') as csv_file:

    csv_data = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\n', quotechar='"', skipinitialspace=True)
    csv_list = list(csv_data)

    for cnt1, cnt2 in zip(range(301,311), range(297,307)):

        print()
        print('{} : {}'.format(cnt1, csv_list[cnt1]))
        print()

        print('{}. 企業名 : {}'.format(cnt1, test_address_book[cnt1].name))
        print('{}. 住所 : {}'.format(cnt1, test_address_book[cnt1].address))
        print()

        if (test_address_book[cnt1].name == address_book[cnt2].name):
            print('企業名が一致しました。')
        else:
            print('{}. 企業名が一致しません : {}'.format(cnt2, address_book[cnt2].name))

        if (test_address_book[cnt1].address == address_book[cnt2].address):
            print('住所が一致しました。')
        else:
            print('{}. 住所が一致しません : {}'.format(cnt2, address_book[cnt2].address))
            
        print()

        print('===================================================')
