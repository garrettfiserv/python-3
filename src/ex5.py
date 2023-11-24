from pprint import pprint
import csv

def build_car_list():
    row_list = []
    solution = []
    with open('files/input.txt') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            row_list.append(row)
    for x in range(1,len(row_list)):
        if "." not in (row_list[x][1]) and (row_list[x][1].isnumeric()):
            solution.append(row_list[x])
    row_list = []
    with open('files/car-ids.txt') as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            row_list.append(row)
        for i in range(len(row_list)):
            for x in range(len(solution)):
                if(row_list[i][0] == solution[x][0]):
                    solution[x].append(row_list[i][1])

    return(solution)
            


def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
