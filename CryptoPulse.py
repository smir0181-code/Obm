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
    canvas.itemconfig(t_label_text, text=name,font=('Arial', 16, 'bold'))

def show_rate_popup(t_name, price_usd, price_rub):
    # Удаляем предыдущие значения
    canvas.delete("price_text")
    
    # Добавляем новые значения с тегом для удаления
    canvas.create_text(200, 180, text=f'{price_usd:.2f} USD', fill='white', font=('Arial', 12,'bold'), tags="price_text")
    canvas.create_text(200, 210, text=f'{price_rub:.2f} RUB', fill='white', font=('Arial', 12,'bold'), tags="price_text")

def exchage():
    t_code = t_combobox.get()
    
    if t_code:
        try:
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={t_code}&vs_currencies=usd,rub')
            response.raise_for_status()
            data = response.json()
            
            if t_code in data:
                price_usd = data[t_code]['usd']
                price_rub = data[t_code]['rub']
                t_name = cryptos[t_code]
                show_rate_popup(t_name, price_usd, price_rub)
            else:
                mb.showerror('Ошибка!', f'Валюта {t_code} не найдена')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')
    else:
        mb.showwarning('Внимание!', 'Выберите криптовалюту')

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
window.title('CryptoPulse')
window.geometry('400x350')

canvas = Canvas(window, width=400, height=350)
canvas.pack(fill='both', expand=True)

for i in range(350):
    color_value = int(50 + (i / 350) * 100)
    color = f'#{color_value:02x}32{min(255, color_value + 50):02x}'
    canvas.create_line(0, i, 400, i, fill=color, width=1)

font_large = ('Arial', 16, 'bold')
font_medium = ('Arial', 12)

canvas.create_text(200, 50, text='Выберите криптовалюту', fill='white', font=font_large)

t_combobox=ttk.Combobox(window, values=list(cryptos.keys()), font=font_medium)
t_combobox.bind("<<ComboboxSelected>>",update_t_label)
canvas.create_window(200, 100, window=t_combobox)

t_label_text = canvas.create_text(200, 140, text='', fill='white', font=font_medium)

button = Button(window, text='Получить курс обмена', bg="#412363", fg='white', font=font_medium, command=exchage)
canvas.create_window(200, 280, window=button)

window.mainloop()