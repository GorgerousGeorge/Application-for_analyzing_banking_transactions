from src.services import transaction_finder


def test_transaction_finder(list_of_transaction):
    assert transaction_finder(list_of_transaction, "супер") == ('[\n'
 '    {\n'
 '        "Описание": "Колхоз",\n'
 '        "Категория": "Супермаркеты"\n'
 '    },\n'
 '    {\n'
 '        "Описание": "Магнит",\n'
 '        "Категория": "Супермаркеты"\n'
 '    }\n'
 ']')

    assert transaction_finder(list_of_transaction, "ко") == ('[\n'
 '    {\n'
 '        "Описание": "Колхоз",\n'
 '        "Категория": "Супермаркеты"\n'
 '    },\n'
 '    {\n'
 '        "Описание": "Константин Л.",\n'
 '        "Категория": "Переводы"\n'
 '    }\n'
 ']')