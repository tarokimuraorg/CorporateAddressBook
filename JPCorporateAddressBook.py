import csv
from ErrorMessageCreator import ErrorMessageCreator
from JPCorporateAddressPage import JPCorporateAddressPage

class JPCorporateAddressBook:

    def __init__(self):

        self._emcreator = ErrorMessageCreator()
        self._csv_list = []

    def readCSVData(self):

        with open('./csv/jigyosyo.csv', 'r', encoding='utf8') as csv_file:

            try:
                csv_data = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\n', quotechar='"', skipinitialspace=True)
                csv_list = list(csv_data)

                return csv_list

            except Exception as e:
                print(self._emcreator.message('JPCorporateAddressBook', 'readCSVData', 'failed to read csv data', '{}'.format(e)))

    def createAddressBook(self):
        
        self._csv_list = self.readCSVData()
        address_book = []
    
        for row in self._csv_list:

            corporate_name = row[2]
            corporate_name = corporate_name.replace('\u3000', ' ')
            corporate_name = corporate_name.replace('（株）', '株式会社')

            corporate_address = row[3] + ' ' + row[4] + ' ' + row[5] + ' ' + row[6]

            address_page = JPCorporateAddressPage(corporate_name, corporate_address)
            address_book.append(address_page)

            """
            print('企業名 : {}'.format(corporate_name))
            print('住所 : {}'.format(corporate_address))
            print(csv_list[cnt])
            print('\n')
            """

        return address_book
