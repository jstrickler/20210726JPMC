
person = ('Bill', 'Gates', 'Microsoft', '1955-10-24')
person = 'Bill', 'Gates', 'Microsoft', '1955-10-24'


print(type(person), len(person), person[0], person[-1])
#  person.first_name  person.last_name      namedtuple

first_name, last_name, product, dob = person
print(first_name, last_name)

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

print(people[0])
print(people[0][0])
print(people[0][0][0])
print()

for person in people:
    print(person[0], person[1])
print()


for person in people:
    first_name, last_name, product, dob = person
    print(first_name, last_name, dob)
print()

for first_name, last_name, product, dob in people:
    # first_name, last_name, product, dob = <next element of person>
    print(first_name, last_name, dob)
print()

items = [(5, 3), (4, 7), (2, 9)]
for a, b in items:
    print(a * b)
print()

