from Func import load_payments, editing_payments, out_data, editing_payments_executed
from os import path
from operator import itemgetter


def main():
    # Получаем отфильтрованный список платежей(без пустых словарей)
    edit_payment = editing_payments(load_payments(path.join('operations.json')))

    # Отбираем выполненные платежи
    edit_payment_executed = editing_payments_executed(edit_payment)

    # Сортируем по дате и выводим пять последних платежей
    edit_payment_executed_sort = sorted(edit_payment_executed, key=itemgetter('date'), reverse=True)
    five_payment = edit_payment_executed_sort[:5]

    """
    Выводим на функцию печати пять последних исполненных платежей
    """
    for item in five_payment:
        if "from" in item.keys():
            out_data(item["date"], item["description"], item["to"], item["operationAmount"]['amount'],
                     item["operationAmount"]['currency']["name"], item["from"])
        else:
            out_data(item["date"], item["description"], item["to"], item["operationAmount"]['amount'],
                     item["operationAmount"]['currency']["name"])


if __name__ == '__main__':
    main()
