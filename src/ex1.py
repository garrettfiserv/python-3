from ValidationException import ValidationException
import csv


def validate_file(input):
    row_list = []
    
    with open(input) as csv_file:
        rows = csv.reader(csv_file, delimiter=',')
        for row in rows:
            row_list.append(row)
    for x in range(1,len(row_list)):
        if "." in (row_list[x][1]) or not (row_list[x][1].isnumeric()):
            raise ValidationException("\nValidationException: " + row_list[x][1] + " is not a valid integer for mileage\n")




def ex1():
    try:
        validate_file("files\input.txt")
    except ValidationException as ve:
        print(ve)

ex1()