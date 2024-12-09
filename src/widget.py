# src/widget.py

def mask_account_card(info):
    # Разделяем строку на тип и номер
    parts = info.rsplit(' ', 1)
    card_type = parts[0]
    number = parts[1]

    if "Счет" in card_type:
        # Маскировка для счета
        masked_number = f"{card_type} **{number[-4:]}"
    else:
        # Маскировка для карт
        masked_number = f"{card_type} {number[:4]} {number[4:6]}** **** {number[-4:]}"

    return masked_number


# src/widget.py

def get_date(date_str):
    # Разделяем строку по символу 'T'
    date_part = date_str.split('T')[0]
    year, month, day = date_part.split('-')
    return f"{day}.{month}.{year}"

