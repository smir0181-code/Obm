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
    canvas.itemconfig(t_label_text, text=name)  # Обновление текста метки на холсте с названием криптовалюты

def show_rate_popup(t_name, price_usd, price_rub):  # Функция создания выпадающего окна с курсом
    popup = Toplevel(window)  # Создание нового окна
    popup.title('Курс обмена')  # Установка заголовка
    popup.geometry('500x400')  # Установка размера окна
    popup.resizable(False, False)  # Запрет изменения размера
    
    # Создание холста для градиентного фона
    popup_canvas = Canvas(popup, width=500, height=400)
    popup_canvas.pack(fill='both', expand=True)
    
    # Создание зеленого градиента
    for i in range(400):
        color_value = int(30 + (i / 400) * 120)
        color = f'#{color_value:02x}{min(255, color_value + 60):02x}{color_value:02x}'
        popup_canvas.create_line(0, i, 500, i, fill=color, width=1)
    
    # Шрифты для выпадающего окна
    title_font = ('Arial', 24, 'bold')  # Крупный шрифт для заголовка
    price_font = ('Arial', 20, 'bold')  # Крупный шрифт для цен
    label_font = ('Arial', 16)  # Средний шрифт для меток
    
    # Отображение информации о курсе
    popup_canvas.create_text(250, 60, text=t_name, fill='white', font=title_font)  # Название криптовалюты
    
    popup_canvas.create_text(250, 140, text='Курс в долларах:', fill='lightgreen', font=label_font)  # Метка USD
    popup_canvas.create_text(250, 170, text=f'${price_usd:.2f} USD', fill='white', font=price_font)  # Цена в USD
    
    popup_canvas.create_text(250, 230, text='Курс в рублях:', fill='lightgreen', font=label_font)  # Метка RUB
    popup_canvas.create_text(250, 260, text=f'{price_rub:.2f} RUB', fill='white', font=price_font)  # Цена в RUB
    
    # Кнопка закрытия
    close_btn = Button(popup, text='Закрыть', bg='#2d5a2d', fg='white', font=('Arial', 14), command=popup.destroy)
    popup_canvas.create_window(250, 330, window=close_btn)
    
    popup.transient(window)  # Привязка к главному окну
    popup.grab_set()  # Модальность окна

def exchage():  # Функция получения и отображения курса криптовалюты
    t_code = t_combobox.get()  # Получение выбранного кода криптовалюты
    
    if t_code:  # Проверка, что криптовалюта выбрана
        try:  # Начало блока обработки исключений
            response = requests.get(f'https://api.coingecko.com/api/v3/simple/price?ids={t_code}&vs_currencies=usd,rub')  # HTTP-запрос к API CoinGecko для получения курса в USD и RUB
            response.raise_for_status()  # Проверка успешности запроса
            data = response.json()  # Преобразование ответа в JSON
            
            if t_code in data:  # Проверка наличия данных о криптовалюте
                price_usd = data[t_code]['usd']  # Извлечение цены в долларах
                price_rub = data[t_code]['rub']  # Извлечение цены в рублях
                t_name = cryptos[t_code]  # Получение полного названия криптовалюты
                show_rate_popup(t_name, price_usd, price_rub)  # Показ кастомного выпадающего окна с курсом
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
window.geometry('400x350')  # Установка размеров окна (ширина x высота)

# Создание холста для градиентного фона
canvas = Canvas(window, width=400, height=350)
canvas.pack(fill='both', expand=True)

# Создание зеленого градиента
for i in range(350):
    color_value = int(50 + (i / 350) * 100)  # Градиент от темно-зеленого к светло-зеленому
    color = f'#{color_value:02x}{min(255, color_value + 50):02x}{color_value:02x}'
    canvas.create_line(0, i, 400, i, fill=color, width=1)

# Создание шрифтов
font_large = ('Arial', 16, 'bold')  # Крупный шрифт для заголовка
font_medium = ('Arial', 12)  # Средний шрифт для текста

# Размещение элементов на холсте
canvas.create_text(200, 50, text='Выберите криптовалюту', fill='white', font=font_large)  # Заголовок на холсте

t_combobox=ttk.Combobox(window, values=list(cryptos.keys()), font=font_medium)  # Создание выпадающего списка с увеличенным шрифтом
t_combobox.bind("<<ComboboxSelected>>",update_t_label)  # Привязка события выбора к функции обновления метки
canvas.create_window(200, 100, window=t_combobox)  # Размещение combobox на холсте

t_label_text = canvas.create_text(200, 150, text='', fill='white', font=font_medium)  # Создание текстовой метки на холсте

button = Button(window, text='Получить курс обмена', bg='#2d5a2d', fg='white', font=font_medium, command=exchage)  # Создание кнопки с темно-зеленым фоном
canvas.create_window(200, 220, window=button)  # Размещение кнопки на холсте
canvas.create_text(200, 50, text='Выберите криптовалюту', fill='white', font=font_large)

window.mainloop()  # Запуск главного цикла обработки событий GUI