from src.masks import get_mask_card_number


def test_get_mask_card_number(mask_card_number):
    assert get_mask_card_number("7556 7748 8893 8885") == mask_card_number
