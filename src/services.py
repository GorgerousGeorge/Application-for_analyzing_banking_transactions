from datetime import datetime
from pandas import DataFrame
import json
import pandas as pd


def transaction_finder(transactions_data: DataFrame) -> json:
    """Принимает на вход датафрейм с банковскими транзакциями. Возвращает json со всеми транзакциями, содержащими
    пользовательский запрос в описании или категории."""
    print("Введите описание того, что мы ищем")
    descr = input()
    descr = descr.lower()
#     report_frame = transactions_data.loc[(descr in transactions_data["Описание"]) |
#                                          (descr in transactions_data["Категория"])]
#     report_dict = report_frame.to_dict("index")
#     report_list = []
#     for value in report_dict.values():
#         report_list.append(value)
#     for transaction in report_list:
#         transaction["Дата платежа"] = transaction["Дата платежа"].strftime("%d.%m.%Y")
#     report_json = json.dumps(report_list, ensure_ascii=False, indent=4)
#     return report_json
#
# testingdata_1 = pd.DataFrame({"Описание": ["Колхоз", "Магнит", "Незнайка", "Макдак"],
#                          "Категория":["Супермаркеты", "Супермаркеты", "Канцтовары", "Фастфуд"]})
#
# transaction_finder(testingdata_1)
