from src.processing import filter_by_state, sort_by_date

# Пример данных для тестов
transactions = [
    {"date": "2024-12-01", "state": "EXECUTED"},
    {"date": "2024-11-30", "state": "PENDING"},
    {"date": "2024-12-02", "state": "EXECUTED"},
    {"date": "2024-11-29", "state": "EXECUTED"},
]

# Тесты для функции filter_by_state
def test_filter_by_state():
    # Проверка фильтрации по состоянию 'EXECUTED'
    executed_transactions = filter_by_state(transactions, 'EXECUTED')
    assert len(executed_transactions) == 3
    assert all(tx['state'] == 'EXECUTED' for tx in executed_transactions)

    # Проверка фильтрации по состоянию 'PENDING'
    pending_transactions = filter_by_state(transactions, 'PENDING')
    assert len(pending_transactions) == 1
    assert pending_transactions[0]['state'] == 'PENDING'

    # Проверка фильтрации по состоянию, которого нет в списке
    unknown_transactions = filter_by_state(transactions, 'UNKNOWN')
    assert len(unknown_transactions) == 0

# Тесты для функции sort_by_date
def test_sort_by_date():
    # Проверка сортировки по дате по умолчанию (убывание)
    sorted_transactions = sort_by_date(transactions)
    assert sorted_transactions[0]['date'] == '2024-12-02'
    assert sorted_transactions[-1]['date'] == '2024-11-29'

    # Проверка сортировки по дате в порядке возрастания
    sorted_transactions_asc = sort_by_date(transactions, reverse=False)
    assert sorted_transactions_asc[0]['date'] == '2024-11-29'
    assert sorted_transactions_asc[-1]['date'] == '2024-12-02'

