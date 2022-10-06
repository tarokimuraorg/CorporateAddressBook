import csv
from ErrorMessageCreator import ErrorMessageCreator
from JPCorporateAddressPage import JPCorporateAddressPage

class TestJPCorporateAddressBook:

    def __init__(self):

        self._emcreator = ErrorMessageCreator()
        self._csv_list = []

    def __readCSVData(self):

        with open('./csv/jigyosyo.csv', 'r', encoding='utf8') as csv_file:

            try:

                csv_data = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\n', quotechar='"', skipinitialspace=True)
                self._csv_list = list(csv_data)

            except Exception as e:

                raise ValueError(self._emcreator.message('TestJPCorporateAddressBook', 'readCSVData', 'failed to read csv data', '{}'.format(e)))

    def createAddressBook(self):

        try:

            self.__readCSVData()
            address_book = []
    
            for row in self._csv_list:

                corporate_name = str(row[2])
                corporate_name = self.__corporateNameConvertor(corporate_name)
                corporate_name = corporate_name.strip()

                corporate_address = str(row[3]) + ' '
                corporate_address = corporate_address + str(row[4]) + ' '
                corporate_address = corporate_address + str(row[5]) + ' '
                corporate_address = corporate_address + str(row[6])
                corporate_address = corporate_address.strip()

                address_page = JPCorporateAddressPage(corporate_name, corporate_address)
                address_book.append(address_page)

            return address_book

        except ValueError as ve:

            print('{}'.format(ve))
            return []

    def __corporateNameConvertor(self, corporate_name : str) -> str:

        result = corporate_name.replace('\u3000', ' ')
        result = result.replace('（株）', '株式会社')
        result = result.replace('（社）', '社団法人')

        return result
