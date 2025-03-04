import json
import logging
from datetime import datetime, timedelta

from pandas import DataFrame

from src.decorators import reportwriter

logger = logging.getLogger("reports")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs\\reports.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname): %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


@reportwriter()
def sending_by_category(transactions_data: DataFrame, categoryname: str, date: datetime = datetime.now()) -> json:
    """Функция возвращает траты по заданной категории за последние три месяца от переданной даты в переданном
    датафрейме с транзакциями. Если дата не передана, то по умолчанию используется текущая"""
    logger.info(f"Начали поиск транзакций за 3 месяца по категории '{categoryname}'")
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
    logger.info(f"Завершили поиск транзакций за 3 месяца по категории '{categoryname}'")
    return report_json
