import pytest


@pytest.fixture
def mask_account():
    return "**5446"


@pytest.fixture
def mask_card_number():
    return "7556 77** **** 8885"

@pytest.fixture
def sample_data():
    """Типовой набор данных для тестов."""
    return [
        {"id": 1, "state": "EXECUTED", "amount": 100},
        {"id": 2, "state": "CANCELED", "amount": 200},
        {"id": 3, "state": "EXECUTED", "amount": 300},
        {"id": 4, "state": "PENDING", "amount": 400},
        ]

@pytest.fixture
def data():
    return "2024-12-31"


@pytest.fixture
def acc_or_card():
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def date():
    return "11.03.2024"