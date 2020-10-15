def filter_long_words(lwords):
    control_number = int(input('Enter the base number here:'))
    longer_words = d
    for i in lwords:
         if len(i) > control_number:
            longer_words.append([i])
    return longer_words

print(filter_long_words(['apple', 'orange', 'banana']))