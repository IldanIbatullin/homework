def get_mask_card_number(card_number: str) -> str:
    if len(card_number) != 16:
        raise ValueError("Неверный формат номера карты")
    return f"**** **** **** {card_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    if len(account_number) != 20:
        raise ValueError("Неверный формат номера счета")
    return f"{account_number[:5]}**** **** **** ****"



