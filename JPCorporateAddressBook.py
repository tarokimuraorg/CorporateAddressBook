import pandas
from ErrorMessageCreator import ErrorMessageCreator
from JPCorporateAddressPage import JPCorporateAddressPage

class JPCorporateAddressBook:
    
    def __init__(self):

        self._emcreator = ErrorMessageCreator()
        self._csv_list = []

    def __readCSVData(self):
        
        try:

            data_frame = pandas.read_csv('./csv/jigyosyo.csv', usecols=[2,3,4,5,6], names=['name','address1','address2','address3','address4'])
            csv_data = data_frame.drop_duplicates()
            self._csv_list = csv_data.values.tolist()

        except Exception as e:

            raise ValueError(self._emcreator.message('JPCorporateAddressBook', 'readCSVData', 'failed to read csv data', '{}'.format(e)))

    def createAddressBook(self):
        
        try:

            self.__readCSVData()
            address_book = []

            for row in self._csv_list:

                corporate_name = str(row[0])
                corporate_name = corporate_name.replace('\u3000', ' ')
                corporate_name = corporate_name.replace('（株）', '株式会社')
                corporate_name = corporate_name.strip()

                corporate_address = str(row[1]) + ' '
                corporate_address = corporate_address + str(row[2]) + ' '
                corporate_address = corporate_address + str(row[3]) + ' '
                corporate_address = corporate_address + str(row[4])
                corporate_address = corporate_address.strip()

                address_page = JPCorporateAddressPage(corporate_name, corporate_address)
                address_book.append(address_page)

            return address_book

        except ValueError as ve:

            print('{}'.format(ve))
            return []
