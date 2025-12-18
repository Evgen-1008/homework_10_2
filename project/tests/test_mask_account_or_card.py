from src.widget import mask_account_or_card
import pytest


def test_mask_account_or_card(acc_or_card):
    # Тест для банковской карты (16 цифр)
    card_input = "Visa Platinum 7000792289606361"
    assert mask_account_or_card(card_input) == acc_or_card