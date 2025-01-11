import os
import json


def reportwriter(filename: str = "Lastreport.json"):
    """Декоратор, который записывает в файл результат, который возвращает функция, формирующая отчет."""

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not os.path.isdir(f"{os.path.dirname(os.getcwd())}\\reports"):
                os.mkdir(f"{os.path.dirname(os.getcwd())}\\reports")
            with open(f"{os.path.dirname(os.getcwd())}\\reports\\{filename}", "w") as file:
                json.dump(result, file, ensure_ascii=False)
            return result

        return wrapper

    return decorator
