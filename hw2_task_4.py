my_line = input("Введите нескольких слов, разделённых пробелами ")
my_list = my_line.split()
for i, el in enumerate(my_list):
    print(i+1, el[0:10])