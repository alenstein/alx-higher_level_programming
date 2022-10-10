#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for index in range(list_length):
        try:
            ans = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
            ans = 0
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            pass
        new_list.append(ans)
    return new_list
