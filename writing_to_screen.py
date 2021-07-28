a = "Justin Bieber"
b = 48.230928342039
c = 5
print(a)
print(a, b)
print(a, b, c)
# print(str(a) + ' ' + str(b) + ' ' + str(c) + '\n')
# print(str(a) + sep + str(b) + sep + str(c) + end)

print(a)
print(b)
print(c)
print(a, b, c, sep="/")
print(a, b, c, sep=", ")
print(a, b, c, sep="")
print(a, end="==>")
# if ...
#   print(...)
print(b, end="==>")
print(c)
print(a, b, end=" ")
print(c)

print(b)
print("a is {} b is {:.2f}".format(a, b))
print(f"a is {a} b is {b:.2f}")  # version 3.6+
