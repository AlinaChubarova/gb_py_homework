keys_list = ["название", "цена", "количество", "ед"]
li = []
n = 0
while n < 4:
    item_data = input("Введите, разделяя пробелом, следующие характеристики товара: название, цена, количество, ед ")
    li.append(item_data)
    n = n + 1
print(li)
items_list = [1, 2, 3, 4]
dict = dict(zip(items_list, li))
print(dict)