def is_member(val):
    a = [1,2,3,4,5]
    for i in a:
        if val == i:
            return True
        else:
            continue
    if val != i:
        return False

print(is_member(6))