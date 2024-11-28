# Проект: Обработка банковских операций

## Описание
Этот проект содержит функции для фильтрации и сортировки банковских операций на основе их состояния и даты.

## Использование
Импортируйте функции из модуля `processing`:

```python
from src.processing import filter_by_state, sort_by_date
transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

executed_transactions = filter_by_state(transactions)
print(executed_transactions)
sorted_transactions = sort_by_date(transactions)
print(sorted_transactions)