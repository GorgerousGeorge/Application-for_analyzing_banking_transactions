import pytest
import pandas as pd
from datetime import datetime


@pytest.fixture
def test_dataframe():
    return pd.DataFrame({"Дата платежа": [datetime(2025, 1, 5, 0, 0, 0),
                                          datetime(2024, 12, 20, 0, 0, 0),
                                          datetime(2024, 8, 6, 0, 0, 0),
                                          datetime(2024, 7, 6, 0, 0, 0),],
                         "Категория":["Супермаркеты", "Супермаркеты", "Канцтовары", "Фастфуд"]})


@pytest.fixture
def test_dataframe_second():
    return pd.DataFrame({"Описание": ["Колхоз", "Магнит", "Незнайка", "Макдак"],
                         "Категория":["Супермаркеты", "Супермаркеты", "Канцтовары", "Фастфуд"]})


@pytest.fixture
def list_of_transaction():
    return [{"Описание":"Колхоз", "Категория": "Супермаркеты"}, {"Описание":"Магнит", "Категория": "Супермаркеты"},
            {"Описание":"Ozon.ru", "Категория": "Различные товары"},
            {"Описание":"Константин Л.", "Категория": "Переводы"}]