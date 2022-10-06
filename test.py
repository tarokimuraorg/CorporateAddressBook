import csv
from JPCorporateAddressBook import JPCorporateAddressBook
from TestJPCorporateAddressBook import TestJPCorporateAddressBook

test_address_book = TestJPCorporateAddressBook().createAddressBook()
address_book = JPCorporateAddressBook().createAddressBook()

with open('./csv/jigyosyo.csv', 'r', encoding='utf8') as csv_file:

    csv_data = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\n', quotechar='"', skipinitialspace=True)
    csv_list = list(csv_data)

    #print('件数 : {}'.format(len(csv_list)))

    for cnt1, cnt2 in zip(range(112,122), range(110,120)):

        print()
        print('{} : {}'.format(cnt1, csv_list[cnt1]))
        print()

        print('{}. 企業名 : {}'.format(cnt1, test_address_book[cnt1].name))
        print('{}. 住所 : {}'.format(cnt1, test_address_book[cnt1].address))
        print()

        if (test_address_book[cnt1].name == address_book[cnt2].name
            and test_address_book[cnt1].address == address_book[cnt2].address):

            print('企業名と住所が一致しました。')

        else:
            print('企業名と住所が一致しません。')
        
        print()

        print('===================================================')
