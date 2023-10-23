#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    j = 0
    lst = []
    while j < list_length:
        try:
            res = my_list_1[j] / my_list_2[j]
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            lst.append(res)
        j += 1
    return lst

