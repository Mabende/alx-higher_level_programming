#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            result_list.append(result)
        except ZeroDivisionError:
            result_list.append("Error: Division by zero")
        except (IndexError, TypeError):
            result_list.append("Error")
    return (result_list)
