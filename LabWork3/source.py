import requests
import datetime

# Получение данных с сайта Центрального банка РФ
response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = response.json()

usd_rate = data['Valute']['USD']['Value']
date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open('data.txt', 'w') as file:
    file.write(f'{date}, CD_RF, {usd_rate}\n')
 