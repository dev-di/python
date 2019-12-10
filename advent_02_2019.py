import csv

inputList = []
with open('input/advent_input_02.txt') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        inputList=row

inputList = [int(i) for i in inputList]
print(inputList)

#pre process the list
inputList[1]=12
inputList[2]=2

#inputList = [1,9,10,3,2,3,11,0,99,30,40,50]
#inputList = [1,1,1,4,99,5,6,0,99]
operationDict={1:'Add', 2:'Multiply', 99:'Exit'}

index=0
operation=operationDict.get(inputList[index])
print('First operation is: {0}'.format(operation))

while not operation.capitalize() == 'Exit':
    parameterIndex1=inputList[index+1]
    parameterIndex2=inputList[index+2]
    resultIndex=inputList[index+3]
    
    if operation.upper() == 'ADD':
        inputList[resultIndex] = inputList[parameterIndex1]+inputList[parameterIndex2]
    elif operation.upper() == 'MULTIPLY':
        inputList[resultIndex] = inputList[parameterIndex1]*inputList[parameterIndex2]
    else:
        print('Unknown operation')

    print('{0} {1} {2} = {3}'.format(inputList[parameterIndex1],operation,inputList[parameterIndex2], inputList[resultIndex]))

    #Next operation
    index=index+4
    operation=operationDict.get(inputList[index])

print(inputList)
print('First value: {0}'.format(inputList[0]))