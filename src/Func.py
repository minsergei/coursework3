import json


def load_payments(data):
    """
    Загружает список платежей из файла
    """
    with open(data) as file:
        payments = json.load(file)
    return payments


def editing_payments(payments):
    """
    Убираем пустые платежи
    """
    count = 0
    a = []
    for item in range(len(payments)):
        if payments[item] == {}:
            zor = item - count
            a.append(zor)
            count += 1
    for item in a:
        del payments[item]
    return payments


def editing_payments_executed(edit_payment):
    """
    Отбираем выполненные платежи
    """
    edit_payment_executed = []
    for item in edit_payment:
        if item["state"] == "EXECUTED":
            edit_payment_executed.append(item)
    return edit_payment_executed


def out_data(date, description, to_data, summ, name_currency, from_data=""):
    """
    Функция печати отобранных платежей
    """
    if from_data == "":
        print(f"{date[:10].replace('-', '.')} {description}\n"
              f"{' '.join(to_data.split(' ')[:-1])} **{to_data[-4:]}\n"
              f"{summ} {name_currency}\n")
    else:
        print(f"{date[:10].replace('-', '.')} {description}\n"
              f"{' '.join(from_data.split(' ')[:-1])} {from_data[-16:-12]} {from_data[-12:-10]}"
              f"{'*' * len(from_data[-10:-8])} {'*' * len(from_data[-8:-4])} {from_data[-4:]}"
              f" -> {' '.join(to_data.split(' ')[:-1])} **{to_data[-4:]}\n"
              f"{summ} {name_currency}\n")
