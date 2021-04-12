month_number = int(input("Введите номер месяца в виде целого числа от 1 до 12 "))
month_list = ["", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
checks = [month_number >= 1, month_number <= 12]
if all(checks):
    print(f"Номеру {month_number} соответствует месяц - {month_list[month_number]}")
else:
    print("Месяца с таким номером нет")

month_number = int(input("Введите номер месяца в виде целого числа от 1 до 12 "))
month_dict = {1: "Январь", 2: "Февраль", 3: "Март", 4: "Апрель", 5: "Май", 6: "Июнь", 7: "Июль", 8: "Август", 9: "Сентябрь", 10: "Октябрь", 11: "Ноябрь", 12: "Декабрь"}
checks = [month_number >= 1, month_number <= 12]
if all(checks):
    print(f"Номеру {month_number} соответствует месяц - {month_dict.get(month_number)}")
else:
    print("Месяца с таким номером нет")