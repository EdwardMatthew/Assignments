def find_longest_word(lwords):
    word_length = []
    for i in lwords:
        word_length.append((len(i), i))
    word_length.sort()
    return word_length[-1][1]

print(find_longest_word(['apple', 'banana', 'hippopotamus']))