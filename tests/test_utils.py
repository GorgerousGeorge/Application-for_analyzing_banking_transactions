import pytest

from src.utils import filter_data
from src.utils import calculate_expenses_and_income


@pytest.mark.parametrize("date, interval, expected_rezult", [
    ("02.03.2025", "W", ["24.02.2025", "02.03.2025"]),
    ("02.03.2025", "M", ["01.03.2025", "02.03.2025"]),
    ("02.03.2025", "Y", ["01.01.2025", "02.03.2025"]),
    ("02.03.2025", "ALL", ["01.01.1900", "02.03.2025"]),
])
def test_times_in_greetings_correct(date, interval, expected_rezult):
    interval_date = filter_data(date, interval)
    assert interval_date[0].strftime("%d.%m.%Y") == expected_rezult[0]
    assert interval_date[1].strftime("%d.%m.%Y") == expected_rezult[1]


def test_calculate_expenses_and_income(testing_dataframe_3):
    interval_date = filter_data("28.02.2025", "M")
    assert (calculate_expenses_and_income(testing_dataframe_3, interval_date[0], interval_date[1]) ==
            (542.37,
             [('Переводы', 381.48), ('Супермаркеты', 160.89)],
             0,
             [('Переводы', 381.48)],
             0,
             []))


def test_calculate_expenses_and_income_second(testing_dataframe_4):
    interval_date = filter_data("28.02.2025", "Y")
    testing_data = (calculate_expenses_and_income(testing_dataframe_4, interval_date[0], interval_date[1]))
    assert testing_data[0] == 11259.26
    assert testing_data[1] == [('Наличные', 8000.0),
                               ('Переводы', 1950.0),
                               ('Другое', 381.48),
                               ('Канцтовары', 349.0),
                               ('Каршеринг', 257.89),
                               ('Супермаркеты', 160.89),
                               ('Фастфуд', 120.0)]
    assert testing_data[2] == 40.0
    assert testing_data[3] ==  [('Наличные', 8000.0),
                                ('Переводы', 1950.0)]
    assert testing_data[4] == 8046.0
    assert testing_data[5] == [('Пополнения', 5546.0),
                               ('Переводы', 2500.0)]
