import json
import pandas as pd
import os
from datetime import datetime, timedelta
from collections import defaultdict

data_path = f"{os.path.dirname(os.getcwd())}\\data\\operations.xlsx"


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
        start_date = end_date - timedelta(days=end_date.weekday())
    elif range_type == 'M':
        start_date = datetime(date.year, date.month, 1)
    elif range_type == 'Y':
        start_date = datetime(date.year, 1, 1)
    elif range_type == 'ALL':
        start_date = datetime(1900, 1, 1)
    else:
        start_date = datetime(date.year, date.month, 1)

    return start_date, end_date


def calculate_expenses_and_income(df, start_date: str, end_date: str):
    """Функция принимает на вход датафрейм с транзакциями, начальную и конечную даты в строковом формате дд.мм.гггг.
    Возвращает: общую сумму расходов; список с 7 основными категориями расходов, отсортированных по убыванию; сумму
    расходов из категорий, не вошедших в 7 основных; сумму расходов в категориях "Переводы" и "Наличные"; общую сумму
    пополнений; список категорий в которых проходили пополнения с сортировкой по убыванию"""
    total_expenses = 0
    total_income = 0
    category_expenses = defaultdict(float)
    category_income = defaultdict(float)
    cash_and_transfer_expenses = defaultdict(float)

    for _, row in df.iterrows():
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
    sorted_cash_and_transfer = sorted(cash_and_transfer_expenses.items(), key=lambda x: x[1], reverse=True)

    main_expenses = sorted_expenses[:7]
    other_expenses = sum(amount for category, amount in sorted_expenses[7:])

    total_expenses = round(total_expenses, 2)

    return total_expenses, main_expenses, other_expenses, sorted_cash_and_transfer, total_income, sorted_income


if __name__ == "__main__":
    print(filter_data("02.03.2025", "M"))
