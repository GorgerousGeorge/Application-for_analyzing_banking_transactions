from datetime import datetime, timedelta
from pandas import DataFrame
import json


def sending_by_category(transactions_data: DataFrame, categoryname: str, date: datetime=datetime.now()) -> json:
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
    report_json = json.dumps(report_list, ensure_ascii=False, indent=4)
    return report_json
