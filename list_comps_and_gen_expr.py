fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach"]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

#    [ EXPR for VAR in ITERABLE if COND]
f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

#  a if b else c
f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

food = ['spam ', 'spam', ' eggs', ' bacon', 'toast', ' spam', 'spam', 'spam ']
food = [f.strip().upper() for f in food]
print("clean food:", food, '\n')


f3 = [f for f in fruits if f.startswith('p')]
print("f3:", f3, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]
last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

tags = [f.upper()[:3] for f in fruits if 'a' in f]
print(tags)

food_gen = (f.strip().upper() for f in food)  # generator expression
print(food_gen)
for food in food_gen:
    print(food)
print()
