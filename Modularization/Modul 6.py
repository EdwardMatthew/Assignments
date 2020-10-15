def histogram(lst):
    for i in lst:
        output = ''
        times = i
        while times > 0:
            output += '*'
            times -= 1
        shape = print(output)
    return shape
histogram([6,4,6])
