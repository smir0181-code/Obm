from os import name  # Импорт переменной name из модуля os (не используется)
import requests  # Библиотека для HTTP-запросов к API
import json  # Библиотека для работы с JSON (не используется)
import pprint  # Библиотека для красивого вывода данных (не используется)
from tkinter import*  # Импорт всех элементов GUI библиотеки tkinter
from tkinter import ttk  # Импорт современных виджетов tkinter
from tkinter import messagebox as mb  # Импорт модуля для диалоговых окон

def update_t_label(event):  # Функция обновления метки при выборе криптовалюты
    code=t_combobox.get()  # Получение выбранного кода криптовалюты из combobox
    name=cryptos[code]  # Получение полного названия по коду из словаря
    t_label.config(text=name)  # Обновление текста метки с названием криптовалюты

def exchage():  # Функция получения и отображения курса криптовалюты
    t_code = t_combobox.get()  # Получение выбранного кода криптовалюты
    
    if t_code:  # Проверка, что криптовалюта выбрана
        try:  # Начало блока обработки исключений
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={t_code}&vs_currencies=usd')  # HTTP-запрос к API CoinGecko
            response.raise_for_status()  # Проверка успешности запроса
            data = response.json()  # Преобразование ответа в JSON
            
            if t_code in data:  # Проверка наличия данных о криптовалюте
                price = data[t_code]['usd']  # Извлечение цены в долларах
                t_name = cryptos[t_code]  # Получение полного названия криптовалюты
                mb.showinfo('Курс обмена', f'Курс: ${price:.2f} USD за {t_name}')  # Показ информационного окна с курсом
            else:  # Если данные не найдены
                mb.showerror('Ошибка!', f'Валюта {t_code} не найдена')  # Показ окна ошибки
        except Exception as e:  # Обработка любых исключений
            mb.showerror('Ошибка', f'Произошла ошибка: {e}')  # Показ окна с описанием ошибки
    else:  # Если криптовалюта не выбрана
        mb.showwarning('Внимание!', 'Выберите криптовалюту')  # Показ предупреждающего окна

cryptos = {  # Словарь с кодами и названиями популярных криптовалют
            'bitcoin': 'Bitcoin (BTC)',  # Биткоин
            'ethereum': 'Ethereum (ETH)',  # Эфириум
            'binancecoin': 'Binance Coin (BNB)',  # Бинанс коин
            'cardano': 'Cardano (ADA)',  # Кардано
            'solana': 'Solana (SOL)',  # Солана
            'ripple': 'Ripple (XRP)',  # Риппл
            'polkadot': 'Polkadot (DOT)',  # Полкадот
            'dogecoin': 'Dogecoin (DOGE)',  # Догикоин
            'shiba-inu': 'Shiba Inu (SHIB)',  # Шиба ину
            'litecoin': 'Litecoin (LTC)'  # Лайткоин
        }

window=Tk()  # Создание главного окна приложения
window.title('CryptoPylse')  # Установка заголовка окна
window.geometry('360x300')  # Установка размеров окна (ширина x высота)

Label(text='Популярные криптовалюты').pack(padx=10,pady=10)  # Создание и размещение текстовой метки
t_combobox=ttk.Combobox(values=list(cryptos.keys()))  # Создание выпадающего списка с кодами криптовалют
t_combobox.bind("<<ComboboxSelected>>",update_t_label)  # Привязка события выбора к функции обновления метки
t_combobox.pack(padx=10, pady=10)  # Размещение combobox в окне с отступами

t_label=ttk.Label()  # Создание пустой метки для отображения названия криптовалюты
t_label.pack(padx=10,pady=10)  # Размещение метки в окне с отступами

Button(text='Получить курс обмена ', command=exchage).pack(padx=10,pady=10)  # Создание и размещение кнопки с привязкой к функции

window.mainloop()  # Запуск главного цикла обработки событий GUI