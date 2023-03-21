import viewA
import datbaseA
def main():
    while True:
        op = viewA.get_op()
        if op == 1:
            data_worker = viewA.get_data()
            datbaseA.add_data(data_worker)
        if op == 2:
            find_str = viewA.find_person()
            datbaseA.find_person(find_str)
        if op == 3:
            worker = viewA.find_person()
            user_lst, full_lst = datbaseA.select_data_person(worker)
            num_line = viewA.choose_str()
            datbaseA.delete_data_person(user_lst, full_lst, num_line)
        if op == 4:
            worker = viewA.find_person()
            user_lst, full_lst = datbaseA.select_data_person(worker)
            num_line = viewA.choose_str()
            data_worker = viewA.get_data()
            datbaseA.change_data_person(user_lst, full_lst, num_line, data_worker)
        if op == 5:
            print("Выход")
            break

