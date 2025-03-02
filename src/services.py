from datetime import datetime
from pandas import DataFrame
import json
import pandas as pd


def transaction_finder(transactions_dict: list[dict], descr:str) -> json:
    """Принимает на вход список словарей с банковскими транзакциями. Возвращает json со всеми транзакциями, содержащими
    пользовательский запрос в описании или категории."""
    list_of_finders = []
    descr = descr.lower()
    for transaction in transactions_dict:
        if descr in transaction["Категория"].lower() or descr in transaction["Описание"].lower():
            list_of_finders.append(transaction)
    return json.dumps(list_of_finders, ensure_ascii=False, indent=4)

