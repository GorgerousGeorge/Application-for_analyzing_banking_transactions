import pytest
from src.reports import sending_by_category
from datetime import datetime

from unittest.mock import Mock
import pandas as pd

def test_sending_by_category_without_date(test_dataframe):
    assert sending_by_category(test_dataframe, "Супермаркеты") == [{
        "Дата платежа": "05.01.2025",
        "Категория": "Супермаркеты"},
        {"Дата платежа": "20.12.2024",
        "Категория": "Супермаркеты"}]
