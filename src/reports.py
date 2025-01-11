from datetime import datetime, timedelta
from pandas import DataFrame
import json
import pandas as pd

testdataframe = pd.DataFrame({"Дата платежа": [datetime(2025, 1, 5, 0, 0, 0),
                                          datetime(2024, 12, 20, 0, 0, 0),
                                          datetime(2024, 8, 6, 0, 0, 0),
                                          datetime(2024, 7, 6, 0, 0, 0),],
                         "Категория":["Супермаркеты", "Супермаркеты", "Канцтовары", "Фастфуд"]})

def sending_by_category(transactions_data: DataFrame, categoryname: str, date=datetime.now()) -> json:
    """Функция возвращает траты по заданной категории за последние три месяца от переданной даты. Если дата не передана,
    то по умолчанию используется текущая"""
    report_date = date - timedelta(days=90)
    report_frame = transactions_data.loc[(transactions_data["Дата платежа"] >= report_date) &
                                         (transactions_data["Категория"] == categoryname)]
    report_dict = report_frame.to_dict("index")
    report_list = []
    for value in report_dict.values():
        report_list.append(value)
    for transaction in report_list:
        transaction["Дата платежа"] = transaction["Дата платежа"].strftime("%d.%m.%Y")
    print(report_list)
    report_json = json.dumps(report_list)
    print(report_json)
    return report_json

sending_by_category(testdataframe, "Супермаркеты")