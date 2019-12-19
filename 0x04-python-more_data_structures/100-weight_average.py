#!/usr/bin/python3
def weight_average(my_list=[]):
    grades = []
    avrage = 0
    if my_list:
        for x in my_list:
            for y in range(x[1]):
                grades.append(x[0])
        for grade in grades:
            avrage += grade
        return avrage / len(grades)
    else:
        return 0
