from os import name
import requests
import json
import pprint 
from tkinter import*
from tkinter import ttk

from tkinter import messagebox as mb

def exchage():
    code = enty.get().upper()
    if code:
        try:
            response=requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data=response.json()
            if code in data['rates']:
                exchage_rate=data['rates'][code]
                #c_name=cur[code]
                mb.showinfo('Курс обмена', f' Курс : {exchage_rate:.2f} {code} за  один доллар' )
            else:
                mb.showerror('Ошибка!', f' Валюта {code} не найдена')
        except Exception as e :
            mb.showerror('ощибка', f'Произошла ошибка : {e}')
    else:
        mb.showwarning('Внимание!', f'введите  код валюты')      
window=Tk()
window.title('Курсы обмена валют')
window.geometry('360x180')
Label(text='Введите код валюты').pack(padx=10,pady=10)
enty=Entry()
enty.pack(padx=10, pady=10)

Button(text='Получить курс обмена к доллару', command=exchage).pack(padx=10,pady=10)

window.mainloop()