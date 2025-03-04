import json
import pandas as pd
import os
from datetime import datetime, timedelta
from collections import defaultdict
import requests
from dotenv import load_dotenv
import logging

load_dotenv()

payload = {}
headers = {
    "apikey": os.getenv("API_KEY")
}

headers_stocks = {'X-Api-Key': os.getenv("STOCK_API_KEY")}

data_path = f"{os.path.dirname(os.getcwd())}\\data\\operations.xlsx"

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs\\utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname): %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def filereader(filepath: str):
    """Вспомогательная функция, которая считывает данные из excel-файла и возвращает dataframe"""
    df = pd.read_excel(filepath)
    return df


def filter_data(date_str: str, range_type: str):
    """Функция, которая устанавливает диапазон дат. На вход принимает строку с конечной датой (в формате дд.мм.гггг) и
    строковый параметр, отвечающий за величину диапазона: W - неделя, на которую приходится дата, M - месяц, Y - год,
    ALL - все данные до указанной даты"""
    date = datetime.strptime(date_str, '%d.%m.%Y')
    end_date = date
    if range_type == 'W':
        logger.info("В качестве диапазона поиска установили неделю")
        start_date = end_date - timedelta(days=end_date.weekday())
    elif range_type == 'M':
        logger.info("В качестве диапазона поиска установили месяц")
        start_date = datetime(date.year, date.month, 1)
    elif range_type == 'Y':
        logger.info("В качестве диапазона поиска установили год")
        start_date = datetime(date.year, 1, 1)
    else:
        logger.info("Пользователь смотрит все операции")
        start_date = datetime(1900, 1, 1)

    return start_date, end_date


def calculate_expenses_and_income(transactions_df, start_date: str, end_date: str):
    """Принимает на вход датафрейм с транзакциями, начальную и конечную даты в строковом формате дд.мм.гггг.
    Возвращает: общую сумму расходов; список с 7 основными категориями расходов, отсортированных по убыванию; сумму
    расходов из категорий, не вошедших в 7 основных; сумму расходов в категориях "Переводы" и "Наличные"; общую сумму
    пополнений; список категорий в которых проходили пополнения с сортировкой по убыванию"""
    total_expenses = 0
    total_income = 0
    category_expenses = defaultdict(float)
    category_income = defaultdict(float)
    cash_and_transfer_expenses = defaultdict(float)
    logger.info("Начали собирать информацию по банковским операциям пользователя и сортировку по категориям")

    for _, row in transactions_df.iterrows():
        transaction_date = datetime.strptime(row['Дата платежа'], '%d.%m.%Y')
        if start_date <= transaction_date <= end_date:
            if row['Сумма платежа'] < 0:
                total_expenses += abs(row['Сумма платежа'])
                category_expenses[row['Категория']] += abs(row['Сумма платежа'])

                if row['Категория'] in ['Наличные', 'Переводы']:
                    cash_and_transfer_expenses[row['Категория']] += abs(row['Сумма платежа'])
            else:
                total_income += row['Сумма платежа']
                category_income[row['Категория']] += row['Сумма платежа']

    sorted_expenses = sorted(category_expenses.items(), key=lambda x: x[1], reverse=True)
    sorted_income = sorted(category_income.items(), key=lambda x: x[1], reverse=True)

    main_expenses = [{'category': category, 'amount': amount} for category, amount in sorted_expenses[:7]]
    other_expenses = sum(amount for category, amount in sorted_expenses[7:])

    sorted_cash_and_transfer = [
        {"category": category, "amount": amount}
        for category, amount in sorted(cash_and_transfer_expenses.items(), key=lambda x: x[1], reverse=True)
    ]

    main_income = [{'category': category, 'amount': amount} for category, amount in sorted_income]

    total_expenses = round(total_expenses, 2)
    logger.info("Завершили сбор информацию по банковским операциям пользователя и сортировку по категориям")

    return total_expenses, main_expenses, other_expenses, sorted_cash_and_transfer, total_income, main_income


def currency_ratings():
    """Функция, которая возвращает текущий курс американского доллара к рублю и евро к рублю"""
    list_of_currencies = []
    valute_code = 'USD'
    url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={valute_code}&amount=1'
    logger.info("Начали собирать информацию по курсам валют")
    while True:
        currency_dict = {}
        currency_dict['currency'] = valute_code
        response = requests.request('GET', url, headers=headers, data=payload)
        currency_dict['rate'] = response.text
        list_of_currencies.append(currency_dict)
        if valute_code == 'EUR':
            logger.info("Завершили сбор информацию о курсах валют")
            return list_of_currencies
        else:
            valute_code = 'EUR'


def stock_pricer():
    """Функция, котрая возвращает курс акций из S&P 500"""
    returned_list = []
    list_of_companies = ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]
    stock_url = 'https://api.api-ninjas.com/v1/stockprice?ticker={}'
    logger.info("Начали собирать информацию по котировкам акций")
    for company in list_of_companies:
        response = requests.get(stock_url.format(company), headers=headers_stocks)
        stock_data = response.json()
        returned_list.append({"stock": company, "price": stock_data["price"]})
    logger.info("Завершили сбор информацию по котировкам акций")
    return returned_list
