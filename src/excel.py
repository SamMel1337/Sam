import csv
import pandas as pd


def tabl_nreg(ter="../data/transactions.csv"):
    list_dict = []
    with open(ter, "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            list_dict.append(row)
        return list_dict


print(tabl_nreg)


def tabl_ger(her="../data/transactions_excel.xlsx"):
    excel_data = pd.read_excel(her)
    excel_data_dict = excel_data.to_dict(orient="records")
    return excel_data_dict


print(tabl_ger)
# transactions = pd.read_csv("../data/transactions.csv", sep=";")
# print(transactions)
