import csv

def create_files(file):
    large_file = open("large-words.txt", "w")
    small_file = open("small-words.txt", "w")
    row_list = []
    word_set = set()
    with open(file) as csv_file:
        rows = csv.reader(csv_file,delimiter=' ')
        for row in rows:
            row_list.append(row)
        all_words = set()
    print (row_list)
    for line in row_list:
        for word in line:
            word_set.add(word)
    word_set.remove('')
    for word in word_set:
        if(len(word) < 3 ):
            small_file.write(word + "\n")
        else:
            large_file.write(word + "\n")
    return len(word_set)


def ex3():
    total_words = create_files("files/words.txt")
    print(f"Total words: {total_words}.")

ex3()