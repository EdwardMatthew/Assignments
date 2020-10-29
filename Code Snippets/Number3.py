# key finder

def findkeys(mydict, val):
    for key in mydict.keys():
        if val in key:
            return True

print(findkeys({'food' : 'bacon'}, ['food']))


