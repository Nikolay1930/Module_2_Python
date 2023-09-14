import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime('%d/%m/%Y')

# url = f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={today}'
# responce = requests.get(url)

url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
responce = requests.get(url, params={'date_req': today})

def get_course(id):
    xml = BeautifulSoup(responce.content, 'html.parser')
    return xml.find('valute', {'id': id}).value.text


# val = '74,7355'[:5]
# val_2 = float('74,7355'.replace(',', '.'))
# print(round(val_2, 2))
# print(val)
# print(f'{get_course("R01239")[:5]} рублей за 1 евро')
# print(f'{get_course("R01235")[:5]} рублей за 1 доллар')
# print(f'{get_course("R01375")[:5]} рублей за 1 китайский юань')

file = open('urok_6.txt', 'w')
file.write(f'{get_course("R01239")[:5]} рублей за 1 евро\n')
file.write(f'{get_course("R01235")[:5]} рублей за 1 доллар\n')
file.write(f'{get_course("R01375")[:5]} рублей за 1 китайский юань')
file.close()


# dict_1 = { 1.4774747447: 1,
#           'key_2': 2}
# print(dict_1)

