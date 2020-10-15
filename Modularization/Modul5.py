def overlapping(lst1, lst2):
    for i in lst1:
        for j in lst2:
            if i == j:
                return True
    else:
        return False

print(overlapping([1,2,3], [3,4,5]))

