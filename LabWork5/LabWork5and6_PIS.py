import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
#импортирование библиотек для дальнешей работы с ними

url_dollar = 'https://quote.ru/ticker/72413'
url_euro = 'https://quote.ru/ticker/59090'
url_yuan = 'https://quote.ru/ticker/59066'
#сохраняю ссылки в переменные для получения данных с этих сайтов

def valuta(url):
    queue = requests.get(url) #получаем запрос
    main_text = queue.text #сохраняем текст запроса
    soup = BeautifulSoup(main_text, 'html.parser') #превращаем ссылку в текст
    course = soup.find('div', {'class': 'MuiGrid-root MuiGrid-item quote-style-1jaw3oe'}) #получаем конкретно курс валюты
    value = course.text #получаем текст
    return value #возвращаем значение необходимое нам
#функция получения курса валюты с сайта и возвращения его стоимости

dollar = valuta(url_dollar)
euro = valuta(url_euro)
yuan = valuta(url_yuan)
#используем функции с данными ссылок

window = tk.Tk()
window.title('Курс валют')
window.geometry('441x200')
#создаем окно приложения

first = tk.Label(window, text = 'Выберите валюту', font = ("Arial", 14))
first.place(x = 130, y = 100)
#создаем текстовую метку

dollar_value = tk.Button(window, width = 20, height = 4, text = 'Доллар', command = lambda: messagebox.showinfo('Доллар', dollar))
dollar_value.place(x = 140, y = 0)
#кнопка доллара

euro_value = tk.Button(window, width = 20, height = 4, text = 'Евро', command = lambda: messagebox.showinfo('Евро', euro))
euro_value.place(x = 0, y = 0)
#кнопка евро

yuan_value = tk.Button(window, width = 20, height = 4, text = 'Юань', command = lambda: messagebox.showinfo('Юань', yuan))
yuan_value.place(x = 290, y = 0)
#кнопка юаня

window.mainloop()
#отображение окна приложения