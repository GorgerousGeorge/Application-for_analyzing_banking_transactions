from datetime import datetime, timedelta
from pandas import DataFrame


def sending_by_category(transactions_data: DataFrame, categoryname: str, date=datetime.datetime.now()):
    """Функция возвращает траты по заданной категории за последние три месяца от переданной даты. Если дата не передана,
    то по умолчанию используется текущая"""
    report_date = date - timedelta(days=90)
    report_frame = transactions_data.loc[transactions_data["Дата платежа"] > report_date]
    return report_frame
