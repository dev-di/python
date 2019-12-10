import csv

def get_csv_line_as_list(input_file):
    INPUT_LIST = []
    with open(input_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            INPUT_LIST=row
    INPUT_LIST = [int(i) for i in INPUT_LIST]
    return INPUT_LIST

def get_csv_lines_as_string_lists(input_file):
    INPUT_LIST = []
    with open(input_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            INPUT_LIST.append(row)
    return INPUT_LIST

def get_integer_lines_as_list(input_file):
    f = open(input_file, 'r')
    textInput = f.readlines()
    f.close()
    res = [int(i) for i in textInput]
    return res