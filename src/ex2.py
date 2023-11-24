import csv

def ex2():
    file_list = ['files/week-1.csv','files/week-2.csv','files/week-3.csv' ]
    total = 0
    row_list = []
    for file in file_list:
        with open(file) as csv_file:
            rows = csv.reader(csv_file, delimiter=',')
            for row in rows:
                row_list.append(row)
        for row in range(1,len(row_list)):
            for col in range(1,len(row_list[0])):
                if(row_list[row][col] == " 1"):
                    total+=1


    print(f"Total visits: {int(total/2)}.")


ex2()