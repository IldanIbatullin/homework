import pytest
from src.processing import (filter_by_state, sort_by_date)
from src.widget import (mask_account_card, get_date)
from src.masks import (get_mask_card_number, get_mask_account)

# Пример данных для тестов
transactions = [
    {"date": "2024-12-01", "state": "EXECUTED"},
    {"date": "2024-11-30", "state": "PENDING"},
    {"date": "2024-12-02", "state": "EXECUTED"},
    {"date": "2024-11-29", "state": "EXECUTED"},
]


# Фикстура для тестов
@pytest.fixture
def sample_transactions():
    return transactions


# Тесты для filter_by_state
def test_filter_by_state(sample_transactions):
    executed_transactions = filter_by_state(sample_transactions, 'EXECUTED')
    assert len(executed_transactions) == 3
    assert all(tx['state'] == 'EXECUTED' for tx in executed_transactions)


# Тесты для sort_by_date
def test_sort_by_date(sample_transactions):
    sorted_transactions = sort_by_date(sample_transactions)
    assert sorted_transactions[0]['date'] == '2024-12-02'
    assert sorted_transactions[-1]['date'] == '2024-11-29'


# Параметризованные тесты для get_mask_card_number
@pytest.mark.parametrize("input_card, expected_output", [
    ("1234567812345678", "************5678"),
    ("1234-5678-1234-5678", "************5678"),
    ("12345", "*****"),
    ("", ""),
])
def test_get_mask_card_number(input_card, expected_output):
    assert get_mask_card_number(input_card) == expected_output


# Параметризованные тесты для get_mask_account
@pytest.mark.parametrize("input_account, expected_output", [
    ("12345678901234567890", "************7890"),
    ("123", "***"),
])
def test_get_mask_account(input_account, expected_output):
    assert get_mask_account(input_account) == expected_output


# Тесты для mask_account_card (пример)
def test_mask_account_card():
    # Пример теста для mask_account_card (необходимо адаптировать под вашу реализацию)
    assert mask_account_card("card") == "masked_card"


# Тесты для get_data (пример)
def test_get_data():
    assert get_date("2024-12-08") == "08/12/2024"