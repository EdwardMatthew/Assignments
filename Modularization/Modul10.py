def pangram_checker(sentence):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabets:
        if i not in sentence.lower():
            return 'This is not a pangram'
        else:
            return 'This is a pangram'

print(pangram_checker('the quick brown fox'))
print(pangram_checker('the quick brown fox jumps over the lazy dog'))