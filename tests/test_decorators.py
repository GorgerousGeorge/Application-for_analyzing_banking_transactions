import pytest
import os
from src.decorators import reportwriter
import json

testreport = [{'сущность': 'тест', 'номер': 1}, {'сущность': 'проверка', 'номер': '2'}]

def test_reportwriter_without_args():
    @reportwriter()
    def some_report():
        return json.dumps(testreport, ensure_ascii=False)

    some_report()
    with open(f"{os.path.dirname(os.getcwd())}\\reports\\Lastreport.json", "r") as file:
        lines = file.readlines()
        assert lines[-1] == ('"[{\\"сущность\\": \\"тест\\", \\"номер\\": 1}, {\\"сущность\\": '
                             '\\"проверка\\", \\"номер\\": \\"2\\"}]"')