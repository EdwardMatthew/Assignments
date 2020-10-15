def makeForming(verb):
    consonant = 'bcdfghjklmnpqrstvwxyz'
    vowels = 'aiueo'
    if verb.endswith('e') and verb not in ['be', 'see', 'flee', 'knee', 'lie']:
        return verb[:-1] + 'ing'
    if verb.endswith('ie'):
        return verb[:-2] + 'ying'
    if verb[0] in consonant and verb[1] in vowels and verb[2] in consonant:
        return verb + verb[2] +'ing'
    else:
        return verb + 'ing'


print(makeForming('lie'))
print(makeForming('see'))
print(makeForming('move'))
print(makeForming('hug'))
