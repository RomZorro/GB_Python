def get_op():
    op = int(input(' 1 - импорт. \n 2 - экспорт. \n 3 - удалить. \n 4 - изменить. \n 5 - выход. \n'))
    return op

def get_data():
    print("Введите новые данные")
    name = input('Имя: ')
    surname = input('Фамилия: ')
    telephone = input('Телефон: ')
    data_str = name + "" + surname + " " + telephone + "\n"
    return data_str

def find_person():
    data_str = input("Введите параметр: ")
    return data_str


def delete_data():
    data_str = input('Введите характеристику для удаления строки: ')
    return data_str

def choose_str():
    answer = int(input("Введите строку, которую нужно изменить: "))
    return answer

# def change_data():
#
#     answer = int(input("Введите строку, которую нужно удалить: "))
#     print("Введите новый параметр: ")
#     new_str = get_data()
#         with open('file.txt', 'w', encoding='UTF-8') as f:
#             for line in lst:
#                 if user_lst[answer - 1] != line:
#                     f.write(line)
#                 else:
#                     f.write(new_str)
#         print('еееее')













