from decimal import Decimal, getcontext
import decimal
#  decimal.Decimal
import math

#  int  float bool complex

i1 = 1000    # dec
i2 = 0b1000  # bin
i3 = 0x1000  # hex
i4 = 0o1000  # oct
print(i1, i2, i3, i4)

x = 2398502935829358293582035982035982039582039582039582323292351075027395017579322435
print(x + 1)

f1 = 123.456
f2  = 123.
f3 = .456
f4 = 5.0
f5 = 1.23432e33
print()

a = 23
b = 7
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)   # floored division -- round down to nearest whole number
print(a ** b)   # raise to power
print(a % b)    # modulus (remainder)


x = 9.3 / 8.3820938238
print(x)
x = round(x, 2)
print(x)

print(math.log2(5))
print(math.log(18))

x = 10
x += 5   # x = x + 5
x *= 4
x /= 3
print(x)

# NOT SUPPORTED:   x++ ++x x-- --x
# for (i = 0; i < 5; i++) { }  NOT IN PYTHON

# sad trombone:
# a = 5
# b = a++
# c = ++a
# print(a, b, c)

#  == != > < >= <= is    "<>"
x = 5
if x is not None:
    print("Wahooo")

# if 'foo' not in x and 'bar' in x:
#     pass
# elif 'thing' not in x:
#     pass
# elif "barf" not in x:
#     pass
# else:
#     pass

x = "12345"

# if all(cond1, cond2, cond3, ...):

#  for ...
#  while ...
import myvars

print(myvars.VALUE)
print(myvars.ANIMAL)

from myvars import VALUE, ANIMAL
print(ANIMAL, VALUE)







