import input_module

INPUT_LIST = input_module.get_csv_line_as_list('input/advent_input_02.txt')

def put_input(list, val1, val2):
    list[1]=val1
    list[2]=val2

operationDict={1:'Add', 2:'Multiply', 99:'Exit'}
def run_integer_program(param1, param2):
    int_list = INPUT_LIST.copy()
    put_input(int_list, param1, param2)
    index=0
    operation=operationDict.get(int_list[index])
    while not operation.capitalize() == 'Exit':
        parameterIndex1=int_list[index+1]
        parameterIndex2=int_list[index+2]
        resultIndex=int_list[index+3]
        
        if operation.upper() == 'ADD':
            int_list[resultIndex] = int_list[parameterIndex1]+int_list[parameterIndex2]
        elif operation.upper() == 'MULTIPLY':
            int_list[resultIndex] = int_list[parameterIndex1]*int_list[parameterIndex2]
        else:
            print('Unknown operation')

        #print('{0} {1} {2} = {3}'.format(inputList[parameterIndex1],operation,inputList[parameterIndex2], inputList[resultIndex]))

        #Next operation
        index=index+4
        operation=operationDict.get(int_list[index])
    return int_list

my_list = INPUT_LIST.copy()

#12,2 -> 9581917

target = 19690720
max_index = 136
for p1 in range(1,max_index):
    for p2 in range (1,max_index):
        res = run_integer_program(p1, p2)
        output = res[0]
        if(output==target):
            print(res)
            print("klar p1 = {0}, p2 = {1}".format(p1, p2))
            break
    if(output==target):
        break