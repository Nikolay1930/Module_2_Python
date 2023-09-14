# from tkinter import *
#
#
# def func():
#     global number
#     lab['text'] = number
#     lab['bg'] = 'black'
#     number += 1
#
#
# number = 1
# window = Tk()
# window.title('Наше приложение')
# window.geometry('500x500+500+100')
#
# lab = Label(window, text='Мой текст', bg='red', fg='#2a664d', font='16')
# lab.place(x=100, y=100)
#
# btn = Button(text='Кнопка', bg='#7b9c8e', fg='red', font='16', command=func)
# btn.place(x=200, y=200)
#
# window.mainloop()


from tkinter import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_course(id):
    xml = BeautifulSoup(responce.content, 'html.parser')
    return xml.find('valute', {'id': id}).value.text






today = datetime.today().strftime('%d/%m/%Y')
url = 'https://www.cbr.ru/scripts/XML_daily.asp?'
responce = requests.get(url, params={'date_req': today})

window = Tk()
window.title('Курс валют')
window.geometry('400x350+400+100')

img = PhotoImage(file='logo.png')
logo = Label(window, image=img)
logo.place(x=0, y=0)

lab = Label(window, text='Курс валют\nMAXI банка', font='Arial 22')
lab.place(y=25, x=150)

course_info = Label(window, text=f"Курс на: {today.replace('/', '.')}",
                    fg='black', font='Arial 18')
course_info.place(y=150, x=90)

usd_label = Label(window, text=f'$ {get_course("R01235")}',
                    fg='black', font='Arial 16')
usd_label.place(y=190, x=100)

eur_label = Label(window, text=f'€ {get_course("R01239")}',
                    fg='black', font='Arial 16')
eur_label.place(y=230, x=100)

window.mainloop()
