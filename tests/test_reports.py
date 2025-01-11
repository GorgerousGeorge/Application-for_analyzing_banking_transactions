import pytest
from src.reports import sending_by_category
from datetime import datetime

from unittest.mock import Mock
import pandas as pd

def test_sending_by_category_without_date(test_dataframe):
    assert sending_by_category(test_dataframe, "Супермаркеты") == ('[\n'
 '    {\n'
 '        "Дата платежа": "05.01.2025",\n'
 '        "Категория": "Супермаркеты"\n'
 '    },\n'
 '    {\n'
 '        "Дата платежа": "20.12.2024",\n'
 '        "Категория": "Супермаркеты"\n'
 '    }\n'
 ']')


def test_sending_by_category_with_date(test_dataframe):
    assert sending_by_category(test_dataframe, "Канцтовары",
                               datetime(2024, 8, 30, 0, 0, 0)) == ('[\n'
 '    {\n'
 '        "Дата платежа": "06.08.2024",\n'
 '        "Категория": "Канцтовары"\n'
 '    }\n'
 ']')


def test_sending_by_category_not_searching_category(test_dataframe):
    assert sending_by_category(test_dataframe, "Фастфуд") == ('[]')
