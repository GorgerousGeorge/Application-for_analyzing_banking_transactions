import json
import logging

logger = logging.getLogger("services")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs\\services.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname): %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def transaction_finder(transactions_dict: list[dict], descr:str) -> json:
    """Принимает на вход список словарей с банковскими транзакциями. Возвращает json со всеми транзакциями, содержащими
    пользовательский запрос в описании или категории."""
    list_of_finders = []
    descr = descr.lower()
    logger.info(f"Начали поиск транзакций по фразе '{descr}'")
    for transaction in transactions_dict:
        if descr in transaction["Категория"].lower() or descr in transaction["Описание"].lower():
            list_of_finders.append(transaction)
    logger.info(f"Завершили поиск транзакций по фразе '{descr}'")
    return json.dumps(list_of_finders, ensure_ascii=False, indent=4)
