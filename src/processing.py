from typing import List, Dict


def filter_by_state(mel1: List[Dict[str, int]], state="EXECUTED") -> list[dict[str, int]]:
    return [mel for mel in mel1 if mel.get("state") == state]


def sort_by_date(ek1: List[Dict[str, int]], reverse: bool = True) -> list[dict[str, int]]:
    return sorted(ek1, key=lambda x: x["date"], reverse=reverse)
