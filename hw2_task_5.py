my_list = [7, 5, 3, 3, 2]
new_item = int(input("Введите новый элемент рейтинга: "))
my_list.sort(reverse=True)
for el in range(len(my_list)):
    if my_list[el] == new_item:
        my_list.insert(el + 1, new_item)
        break
    elif my_list[0] < new_item:
        my_list.insert(0, new_item)
    elif my_list[-1] > new_item:
        my_list.append(new_item)
    elif my_list[el] > new_item > my_list[el + 1]:
        my_list.insert(el + 1, new_item)

print(f"Новый рейтинг - {my_list}")