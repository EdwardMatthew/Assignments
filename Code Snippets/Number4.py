# word frequency calculatro program

def wordfrequencies(mylist):
    freq_counter = {}
    for words in mylist.split(' '):
        if words in freq_counter:
            freq_counter[words] += 1
        else:
            freq_counter[words] = 1
    return freq_counter

print(wordfrequencies('the quick brown fox jumps over the lazy dog while the dog was napping'))