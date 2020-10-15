def makeForms(verb):
    if verb.endswith('y'):
        return verb[:-1] + 'ies'
    if verb.endswith('o') or verb.endswith('ch') or verb.endswith('s') or verb.endswith('sh'):
        return verb + 'es'
    if verb.endswith('x') or verb.endswith('z'):
        return verb + 'es'
    else:
         return verb + 's'

print(makeForms('run'))
print(makeForms('try'))
print(makeForms('brush'))
print(makeForms('fix'))
print(makeForms('stymy'))
