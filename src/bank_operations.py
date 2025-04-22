import re
from src.utils import load_transactions


def filter_operations_by_description(operations, search_string):
    # Компилируем регулярное выражение для поиска
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)  # Игнорируем регистр

    # Фильтруем операции по описанию
    filtered_operations = [
        operation
        for operation in operations
        if "description" in operation and pattern.search(operation["description"])
    ]

    return filtered_operations


operations_data = load_transactions("../data/operations.json")

search_term = "перевод"
filtered_results = filter_operations_by_description(operations_data, search_term)

for i in filtered_results:
    print(filtered_results)
