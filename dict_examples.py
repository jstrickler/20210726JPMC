d1 = dict()   # empty dict
d2 = {'a': 5, 'm': 32, 'e': 18, 'd': 7}
print(d2)
d3 = {}
d2['r'] = 27
print(d2)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(len(airports))
print(airports['MCO'], airports['RDU'], airports['IAD'])

for key in 'RDU', 'LAX', 'YCC', 'ELM', 'SAC':
    print(key, key in airports)
print()

