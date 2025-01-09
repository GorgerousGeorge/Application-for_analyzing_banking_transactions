import json
from datetime import datetime
import pandas as pd


def times_in_greetings(timedate: str) -> str:
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


def common_card_info(transactions_data: xlsx) -> str:
