s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''

x = '"01" 'f''
print(x)
print('Guido\'s the BDFL emeritus of Python')  # avoid this!
print("Guido's the BDFL emeritus of Python")
print('Guido is the "BDFL emeritus" of Python')
print("""Guido's the "BDFL emeritus" of Python""")

query = """
select *
from customer_accounts
where date > '2021-07-01'
and customer_id = '123445'
"""

print(s1, s2, s3, s4)

s5 = r"spam\n"
print(s5, "more stuff")

name = "Lakshmi"
print(f"My name is {name}")    #  Lakme
