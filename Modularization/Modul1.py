def convert_list_and_tuple():
    numbers = input('Enter comma-separated numbers:').split(',')
    list = numbers
    as_tuple = tuple(list)
    output = print('List:', list, '\nTuple:', as_tuple)
    return output

convert_list_and_tuple()







