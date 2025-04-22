import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "top5, top6",
    [
        ("Счет 25090112312345644545", "Счет ** 4545"),
        ("Счет 57747885848894585455665", "Счет Неправильный номер"),
        ("Visa Platinum 7000792289606361", "VisaPlatinum 7000 92** **** 6361"),
    ],
)
def test_add5(top5, top6):
    assert mask_account_card(top5) == top6


@pytest.mark.parametrize("top7, top8", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_add6(top7, top8):
    assert get_date(top7) == top8
