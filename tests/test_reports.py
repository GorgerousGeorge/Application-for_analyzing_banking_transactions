import pytest
from src.reports import sending_by_category

from unittest.mock import Mock
import pandas as pd

def test_sending_by_category():
    mock_frame = pd.dataframe()
