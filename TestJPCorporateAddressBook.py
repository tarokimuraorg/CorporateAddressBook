import csv
from ErrorMessageCreator import ErrorMessageCreator
from JPCorporateAddressPage import JPCorporateAddressPage

class TestJPCorporateAddressBook:

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
            corporate_name = corporate_name.strip()

            corporate_address = row[3] + ' '
            corporate_address = corporate_address + row[4] + ' '
            corporate_address = corporate_address + row[5] + ' '
            corporate_address = corporate_address + row[6]
            corporate_address = corporate_address.strip()

            address_page = JPCorporateAddressPage(corporate_name, corporate_address)
            address_book.append(address_page)

        return address_book
