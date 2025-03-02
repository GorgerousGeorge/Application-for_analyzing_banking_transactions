import json
import pandas as pd
import os
from datetime import datetime, timedelta
from collections import defaultdict

data_path = f"{os.path.dirname(os.getcwd())}\\data\\operations.xlsx"

df = pd.read_excel(data_path)


def filter_data(date_str: str, range_type: str):
    """Функция, которая устанавливает диапазон дат. На вход принимает строку с конечной датой (в формате дд.мм.гггг) и
    строковый параметр, отвечающий за величину диапазона: W - неделя, на которую приходится дата, M - месяц, Y - год,
    ALL - все данные до указанной даты"""
    date = datetime.strptime(date_str, "%d.%m.%Y")
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


if __name__ == "__main__":
    print(filter_data("02.03.2025", "M"))
