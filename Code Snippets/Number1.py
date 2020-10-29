# remove dictionary keys based on list

def removekeys(mydict, keylist):
    for item in keylist:
        if item in mydict:
            mydict.pop(item)
        return mydict

print(removekeys({"brand" : "Ford", "model" : "Mustang", "year" : 1964}, ["brand", "model", "bacon"]))