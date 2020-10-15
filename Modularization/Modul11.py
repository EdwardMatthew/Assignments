def char_freq(string):
    freq_counter = {}
    for i in string:
        if i in freq_counter:
            freq_counter[i] += 1
        else:
            freq_counter[i] = 1
    return freq_counter

print('Character frequency for this string is:')
print(char_freq('apple'))


