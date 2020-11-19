# program for finding hapax legomenons

from string import punctuation

def find_hapax():
    file = open(' monthy python.txt', 'r')
    text = file.read().lower().replace("\n"," ")
    filtered = ""

    for words in text:
        if words not in punctuation:
            filtered += words

    text = filtered
    data = text.split(" ")
    counter = {}

    for i in data:
        if i not in counter:
            counter[i] = 1
        else:
            counter[i] += 1

    hapax_counter = []
    for j in counter:
        if counter[j] == 1:
            hapax_counter.append(j)
    return hapax_counter

print(find_hapax())