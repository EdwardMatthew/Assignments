def translate(text):
    consonants = 'bcdfghjklmnpqrstwxyz'
    return ''.join(l + 'o' + l if l in consonants else l for l in text)

print(translate('this is fun'))