from src.Func import load_payments, editing_payments, editing_payments_executed
from os import path


def test_load_payments():
    assert load_payments(path.abspath("/home/min/coursework3/test.json")) == [{"id": 441945886, "state": "EXECUTED"}]


# pytest --cov src --cov-report term-missing
def test_editing_payments():
    assert editing_payments([{"id": 441945886, "state": "EXECUTED"}, {}]) == [{"id": 441945886, "state": "EXECUTED"}]


def test_editing_payments_executed():
    assert (editing_payments_executed([{"id": 441945886, "state": "EXECUTED"}, {"id": 441945886, "state": "ED"}])
            == [{"id": 441945886, "state": "EXECUTED"}])
