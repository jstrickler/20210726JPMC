list1 = list()
print(list1, len(list1))
cities = ['Taos', 'Santa Fe', 'Albuquerque']
print(cities, len(cities))
print(cities[0])
if 'Taos' in cities:
    print("woohoo")
list2 = []
cities.append("Phoenix")
cities.append("Albany")
print(cities)
cities.insert(0, "Jersey City")
cities.insert(4, "Philadelphia")
cities.insert(1, "Tampa")
print(cities)
more_cities = ["Houston", "Durham", "Charleston"]
cities.append(more_cities)  # as a list

             # iterable (sequence/array etc)
cities.extend(more_cities)  # as individual objects
print(cities)

del cities[4]
print(cities)

cities.remove('Taos')
print(cities)

# cities.remove("Front Royal")   ValueError!
c = cities.pop()  # remove last element and return it
print(c, cities)

c = cities.pop(2)  # remove element with index 2 and return it
print(c, cities)

#  L.append(obj) L.insert(pos, obj)  L.extend(iterable)
#  del L[n]  L.remove(value)   x = L.pop(pos)   x = L.pop()
#   value in L

print(cities.index('Jersey City'))
print(cities.index('Albany'))
print(cities.index(more_cities))

foods = ['spam', 'spam', 'eggs', 'spam', 'spam', 'eggs', 'spam']
del cities[5]
cities.append("Atlanta")
cities.append("Boston")
cities.append("Miami")
print(cities)
print(cities[0])
print(cities[6])
print(cities[-1])   # cities[len(cities)-1]
print(cities[-4])
print(cities[0:4])   # [start:stop]  [:stop] [start:]
print(cities[:4])
print(cities[3:6])  #  items 3, 4, 5
print(cities[-5:])  # last 5

state = "North Dakota"
print(state[:5])
print(state[6:9])
print(state[-4:])
print(len(cities), len(foods))
print(foods.count('eggs'), foods.count('spam'))
print()

for city in cities:
    #  city = <next element of cities>
    print(city.upper())
print()

for food in foods:
    if food != 'spam':
        print(food)
print()

# for VAR in ITERABLE:
#     ...

for city in reversed(cities):
    print(city)

name = "John Strickler"
for char in reversed(name):
    print(char, end='')
print('\n')

print(cities)
print(min(cities), max(cities), sorted(cities))

nums = [800,80,1000,32,255,400,5,5000]

print(min(nums), max(nums), sorted(nums), sum(nums))

items = [(5, 3), (4, 7), (2, 9), (5, 1), (4, 2), (2, 22)]
print(sorted(items), '\n')

data = ['aaa', 'bbb', 'ccc']
for d in data:
    print(d)
print()

for d in reversed(data):
    print(d)
print()

rdata = reversed(data)
print(rdata)
for d in rdata:
    print(d)
print("second time:")
for d in rdata:
    print(d)
print()

print(list(enumerate(data)))

for i, value in enumerate(data):
    print(i, value)
print()

for i in range(5):
    print("Wombats are cuddly")
print()

# range(stop) range(start, stop) range(start, stop, step)
r = range(10)
print(r)
for _ in r:
    print("Python is the coolest!")











