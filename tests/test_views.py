import pandas as pd
import json
from src.views import events

def test_events(testing_dataframe_5):
    result = events(testing_dataframe_5, "07.01.2023")
    response = json.loads(result)

    assert response['expences']['total_amount'] == 150, "Общая сумма расходов должна быть 150"

    assert response['income']['total_amount'] == 500, "Общая сумма доходов должна быть 500"
