#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newList = []
    for x in range(0, list_length):
        try:
            newList.append(my_list_1[x] / my_list_2[x])
        except TypeError:
            print("wrong type")
            newList.append(0)
        except ValueError:
            print("wrong type")
            newList.append(0)
        except ZeroDivisionError:
            print("division by 0")
            newList.append(0)
        except IndexError:
            print("out of range")
            newList.append(0)
        finally:
            pass
    return newList
