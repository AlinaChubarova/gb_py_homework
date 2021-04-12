my_list = list(input("Введите произвольный текст "))
print(my_list)
n = 0
for i in range(int(len(my_list)/2)):
    my_list[n], my_list[n+1] = my_list[n+1], my_list[n]
    n += 2
print(my_list)