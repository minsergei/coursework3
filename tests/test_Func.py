from src.Func import load_payments, editing_payments, editing_payments_executed
from os import path
from pathlib import Path

def test_load_payments():
    operations = Path(__file__).parent.joinpath('test.json')
    assert load_payments(operations) == [{"id": 441945886, "state": "EXECUTED"}]


# pytest --cov src --cov-report term-missing
def test_editing_payments():
    assert editing_payments([{"id": 441945886, "state": "EXECUTED"}, {}]) == [{"id": 441945886, "state": "EXECUTED"}]


def test_editing_payments_executed():
    assert (editing_payments_executed([{"id": 441945886, "state": "EXECUTED"}, {"id": 441945886, "state": "ED"}])
            == [{"id": 441945886, "state": "EXECUTED"}])
