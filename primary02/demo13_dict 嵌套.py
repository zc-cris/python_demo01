# _Author: zc-cris

persons = {
    'info': {
        'name': ['cris', 'james'],
        'age': 23,
        'address': 'USA'
    },
    'major': 'IT',
    'salary': 32302.90
}

persons['info']['age'] = 25
print(persons['info'])

persons['info']['name'][1] = persons['info']['name'][1].upper()
print(persons['info']['name'][1])

persons['info']['name'].append("curry")
print(persons['info']['name'])

persons['info']['female'] = 'man'
print(persons['info'])
