import re
def change_case(identifier, target_case):
    if identifier == '':
        return ''
    if '-' in identifier and '_' in identifier:
        return None
    if any(c.isupper() for c in identifier) and ('_' in identifier or '-' in identifier):
        return None
    if '-' in identifier:
        words = identifier.split('-')
    elif '_' in identifier:
        words = identifier.split('_')
    elif identifier[0].islower() and any(c.isupper() for c in identifier):
        words = re.findall(r'[a-z]+|[A-Z][a-z]*',identifier)
        words = [w.lower() for w in words]
    else:
        return None
    
    if target_case == 'snake':
        return '_'.join(words)
    elif target_case == 'kebab':
        return '-'.join(words)
    elif target_case == 'camel':
        return words[0] + ''.join(word.capitalize() for word in words[1:])
    else:
        return None