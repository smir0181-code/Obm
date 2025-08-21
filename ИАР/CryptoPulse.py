from os import name
import requests
import json
import pprint 
from tkinter import*
from tkinter import ttk

from tkinter import messagebox as mb



def update_t_label(event):
    code=t_combobox.get()
    name=cryptos[code]
    t_label.config(text=name)

def exchage():
    t_code = t_combobox.get()
    
    if t_code :
        try:
            response=requests.get(f'https://api.coingecko.com/api/v3/coins/markets')
            response.raise_for_status()
            data=response.json()
            if t_code in data['rates']:
                exchage_rate=data['rates'][t_code]
                t_name=cryptos[t_code]
                
                mb.showinfo('Курс обмена', f' Курс : {exchage_rate:.2f} {t_name} за  один' )
            else:
                mb.showerror('Ошибка!', f' Валюта {t_code} не найдена')
        except Exception as e :
            mb.showerror('ощибка', f'Произошла ошибка : {e}')
    else:
        mb.showwarning('Внимание!', f'введите  код валюты')
cryptos = {
            'bitcoin': 'Bitcoin (BTC)',
            'ethereum': 'Ethereum (ETH)',
            'binancecoin': 'Binance Coin (BNB)',
            'cardano': 'Cardano (ADA)',
            'solana': 'Solana (SOL)',
            'ripple': 'Ripple (XRP)',
            'polkadot': 'Polkadot (DOT)',
            'dogecoin': 'Dogecoin (DOGE)',
            'shiba-inu': 'Shiba Inu (SHIB)',
            'litecoin': 'Litecoin (LTC)'
        }
window=Tk()
window.title('Курсы обмена криптовалют')
window.geometry('360x300')





Label(text='Популярные криптовалюты').pack(padx=10,pady=10)
t_combobox=ttk.Combobox(values=list(cryptos.keys()))
t_combobox.bind("<<ComboboxSelected>>",update_t_label)
t_combobox.pack(padx=10, pady=10)

t_label=ttk.Label()
t_label.pack(padx=10,pady=10)

Button(text='Получить курс обмена ', command=exchage).pack(padx=10,pady=10)

window.mainloop()