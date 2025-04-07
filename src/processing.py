from typing import List, Dict


def filter_by_state(mel1: List[Dict[str, int]], state="EXECUTED") -> list[dict[str, int]]:
    return [req for req in mel1 if isinstance(req, dict) and req.get("state") == state]


def sort_by_date(ek1: List[Dict[str, int]], reverse: bool = True) -> list[dict[str, int]]:
    return sorted(ek1, key=lambda x: x["date"], reverse=reverse)
