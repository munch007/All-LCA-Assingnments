dict = {'name': 'sanchit', 'prn':1272262076,'course':'core cse'}

print(dict['name'])

print(dict.keys())

print(dict.values())

print(dict.items())

print('name' in dict)

dict['year']=2026
print(dict)

dict['course']='btech cse core'
print(dict)

del dict['year']
print(dict)

tuple = ('sanchit',18,2007)

print(tuple[0])

print(tuple[:2])

print(2007 in tuple)

print(tuple.count(18))

print(tuple.index(2007))

