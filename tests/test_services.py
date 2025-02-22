from src.services import transaction_finder


def test_transaction_finder(list_of_transaction):
    assert transaction_finder(list_of_transaction, "супер") == (
        '[{"Описание": "Колхоз", "Категория": "Супермаркеты"}, {"Описание": "Магнит", "Категория": "Супермаркеты"}]')
    assert transaction_finder(list_of_transaction, "ко") == (
        '[{"Описание": "Колхоз", "Категория": "Супермаркеты"}, {"Описание": "Константин Л.", "Категория": "Переводы"}]')