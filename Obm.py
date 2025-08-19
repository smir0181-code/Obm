from os import name
import requests
import json
import pprint 
from tkinter import*
from tkinter import ttk

from tkinter import messagebox as mb

def exchage():
    try:
        currency=enty.get().upper()
        url=f'https://api.exchangerate-api.com/v4/latest/{currency}'
        response=requests.get(url)
        data=json.loads(response.text)
        rate=data['rates']['USD']
        mb.showinfo('Курс обмена', f'1 {currency} = {rate} USD')
    except:
        mb.showerror('Ошибка', 'Неверный код валюты')

window=Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')
Label(text='Введите код валюты').pack(padx=10,pady=10)
enty=Entry()
enty.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchage).pack(padx=10,pady=10)

window.mainloop()