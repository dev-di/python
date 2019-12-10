import csv

print('python/Hello')

inputList = []
with open('python/advent_input_02.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        inputList=row

print(inputList)