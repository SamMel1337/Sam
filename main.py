from src.utils import load_transactions,convert_transaction_to_rub
from src.excel import tabl_nreg,tabl_ger
from src.processing import sort_by_date,filter_by_state

print(
    """Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
)
user_choice = input("Введите цифру:")
if user_choice == "1":
    transactions = load_transactions("data/operations.json")
    print("Для обработки выбран JSON-файл")
elif user_choice == "2":
        transactions = tabl_nreg("data/transactions.csv")
        print("Для обработки выбран CSV-файл")
elif user_choice == "3":
        transactions = tabl_ger("data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл")
else:
    # если пользователь выбрал что-то некорректно, то по умолчанию можно открыть JSON-файл
    transactions = load_transactions("data/operations.json")
print("""Введите статус, по которому необходимо выполнить фильтрацию. 
        Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
state = input("Введите статус:").upper()
if state in ["EXECUTED", "CANCELED", "PENDING"]:
    print(f"Операции отфильтрованы по статусу {state}")
    transactions = filter_by_state(transactions,state)
else:
    print(f"Некорректный статус{state}")

print("Отсортировать операции по дате? Да/Нет")
answer = input().lower()
if answer == "да":
    print("Отсортировать по возрастанию или по убыванию? Да/Нет")
    reverse = input().lower()
    if reverse == "да":
        transactions = sort_by_date(transactions, reverse=False)
    elif reverse == "Нет":
        transactions = sort_by_date(transactions)
elif answer == "нет":
    transactions = transactions

# Фильтрация только рублевых транзакций

print("Выводить только рублевые транзакции? Да/Нет")
trans= input().lower()
if trans == "Да":
    filtered_rub_transactions = convert_transaction_to_rub(transactions == "RUB")
else:
    filtered_rub_transactions = transactions

# Фильтрация по слову в описании (если требуется)
print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
filtering = input().lower()
if filtering == "Да":
    keyword = input("Введите слово для фильтрации: ").lower()
    filtered_transactions = [t for t in filtered_rub_transactions if keyword.lower() in t.get('description', '').lower()]
else:
    filtered_transactions = filtered_rub_transactions

# Вывод результатов
print(filtered_transactions)

