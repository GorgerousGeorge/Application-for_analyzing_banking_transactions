import json
from datetime import datetime
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame
from src.settings import base_dir
import os


def times_in_greetings(timedate: str) -> str:
    """Принимает на вход строку с датой и временем в формате YYYY-MM-DD HH:MM:SS. Возвращает строку с приветствием,
    в зависимости от времени суток во входящей строке"""
    hour = int(timedate[-8:-6])
    if hour < 4:
        greetings = "Доброй ночи"
    elif 4 < hour < 12:
        greetings = "Доброе утро"
    elif 11 < hour < 18:
        greetings = "Добрый день"
    else:
        greetings = "Добрый вечер"
    print (hour)
    return greetings


def common_card_info(transactions_data: DataFrame) -> list[dict]:
    """Принимает на вход датафрейм с информацией о банковских транзакциях. Возвращает список словарей по каждой карте из
    датафрейма с номером карты, общей суммой расходов и заработанным кэшбэком. В расходах не учитываются переводы и
    пополнения"""
    returned_list = []
    spend_data = transactions_data.loc[(transactions_data["Статус"] == "OK") &
                                       (transactions_data["Категория"] != "Переводы") &
                                       (transactions_data["Категория"] != "Пополнения")]
    spend_data_by_card = spend_data.groupby("Номер карты")
    for spend in spend_data_by_card:
        cardinfo = {}
        cardinfo["last_digits"] = spend["Номер карты"]
        cardinfo["total_spent"] = spend["Сумма платежа"]
        cardinfo["cashback"] = spend["Сумма платежа"] // 100
        returned_list.append(cardinfo)
    result = spend_data_by_card.apply(pd.Series.sum)
    print(returned_list)


testframe = pd.read_excel(base_dir.joinpath("data", "operations.xlsx"))
common_card_info(testframe)


