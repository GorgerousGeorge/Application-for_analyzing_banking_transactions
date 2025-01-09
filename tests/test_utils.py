import pytest

from src.utils import times_in_greetings


@pytest.mark.parametrize("string, expected_rezult", [
    ("YYYY-MM-DD 01:MM:SS", "Доброй ночи"),
    ("YYYY-MM-DD 08:MM:SS", "Доброе утро"),
    ("YYYY-MM-DD 12:MM:SS", "Добрый день"),
    ("YYYY-MM-DD 23:MM:SS", "Добрый вечер"),
])
def test_times_in_greetings_correct(string, expected_rezult):
    assert times_in_greetings(string) == expected_rezult


def test_times_in_greetings_empty():
    with pytest.raises(Exception):
        times_in_greetings("")