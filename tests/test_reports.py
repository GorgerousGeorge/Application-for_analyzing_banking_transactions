import pytest
from src.reports import sending_by_category
from datetime import datetime

from unittest.mock import Mock
import pandas as pd

def test_sending_by_category_without_date(test_dataframe):
    assert sending_by_category(test_dataframe, "Супермаркеты") == pd.DataFrame({
        "Дата платежа": [datetime(2025, 1, 5, 0, 0, 0),
                         datetime(2024, 12, 20, 0, 0, 0)],
        "Категория":["Супермаркеты", "Супермаркеты"]})
