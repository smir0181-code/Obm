from os import name
import requests
import json
import pprint 
from tkinter import*
from tkinter import ttk

from tkinter import messagebox as mb

def update_b_label(event):
    code=b_combobox.get()
    name=cur[code]
    b_label.config(text=name)

def update_t_label(event):
    code=t_combobox.get()
    name=cur[code]
    t_label.config(text=name)


def exchage():
    t_code = t_combobox.get()
    b_code = b_combobox.get()
    if t_code and b_code:
        try:
            response=requests.get(f'https://open.er-api.com/v6/latest/{b_code}')
            response.raise_for_status()
            data=response.json()
            if t_code in data['rates']:
                exchage_rate=data['rates'][t_code]
                t_name=cur[t_code]
                b_name=cur[b_code]
                mb.showinfo('Курс обмена', f' Курс : {exchage_rate:.2f} {t_name} за  один {b_name}' )
            else:
                mb.showerror('Ошибка!', f' Валюта {t_code} не найдена')
        except Exception as e :
            mb.showerror('ощибка', f'Произошла ошибка : {e}')
    else:
        mb.showwarning('Внимание!', f'введите  код валюты')
cur={'RUB':'Российский рубль',
'EUR':'Евро',
'GBP':'Британский фунт стерлингов','JPY':'Японская ена',
'CNY':'Китайский юфнь','KXT':'Казахский тенге',
'UZS':'Узбекский сум','CHF':'Швейцарский франк',
'AED':'Арабский дирхам',
'CAD':'Канадский доллар','USD':'Американский доллар'}    
window=Tk()
window.title('Курсы обмена валют')
window.geometry('360x300')
Label(text='Базовая валюта').pack(padx=10,pady=10)
b_combobox=ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)

b_combobox.bind("<<ComboboxSelected>>",update_b_label)
b_label=ttk.Label()
b_label.pack(padx=10,pady=10)

Label(text='Целевая валюта').pack(padx=10,pady=10)
t_combobox=ttk.Combobox(values=list(cur.keys()))
t_combobox.bind("<<ComboboxSelected>>",update_t_label)
t_combobox.pack(padx=10, pady=10)

t_label=ttk.Label()
t_label.pack(padx=10,pady=10)

Button(text='Получить курс обмена ', command=exchage).pack(padx=10,pady=10)

window.mainloop()