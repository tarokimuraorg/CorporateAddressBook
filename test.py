import csv

with open('./csv/jigyosyo.csv', 'r', encoding='utf8') as csv_file:

    csv_data = csv.reader(csv_file, delimiter=',', doublequote=True, lineterminator='\n', quotechar='"', skipinitialspace=True)
    csv_list = list(csv_data)

    #print('件数 : {}'.format(len(csv_list)))

    for cnt in range(0,10):

        corporate_name = csv_list[cnt][2]
        corporate_name = corporate_name.replace('\u3000', ' ')
        corporate_name = corporate_name.replace('（株）', '株式会社')

        corporate_address = csv_list[cnt][3] + ' ' + csv_list[cnt][4] + ' ' + csv_list[cnt][5] + ' ' + csv_list[cnt][6]

        print('企業名 : {}'.format(corporate_name))
        print('住所 : {}'.format(corporate_address))
        print(csv_list[cnt])
        print('')
