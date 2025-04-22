import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "top1, top2",
    [
        ("23030012312345645601", "** 5601"),
        ("21231231231231321332123", "Неправильный номер"),
        ("", "Неправильный номер"),
    ],
)
def test_add(top1, top2):
    assert get_mask_account(top1) == top2


@pytest.mark.parametrize(
    "top3, top4",
    [
        ("2303200025092001", "2303 00** **** 2001"),
        ("234324234242342443", "Неправильный номер"),
        ("", "Неправильный номер"),
    ],
)
def test_add1(top3, top4):
    assert get_mask_card_number(top3) == top4
