actor = "Chris Hemsworth"
print(len(actor), type(actor))

print(actor.upper())
a1 = actor.upper()
print(a1)

# Class.method()
# instance.method()

print(actor + actor.lower())
a = "wom"
b = "bat"
print(a + b)
print(actor)
print(actor.count('h'))
print(actor.lower().count('h'))
print(actor.startswith('Chris')) # actor.endswith(...)
print(actor.startswith('Liam'))
print(actor.find('Chris'))
print(actor.find('Liam'))
print(actor.find('worth'))
print("Hem" in actor)  # LIKE actor.contains("Hem")
print("Haw" in actor)

print(actor.replace('Chris', 'Liam'))
print(actor.replace('h', 'X'))
print(actor.replace('h', 'X', 1))

s = "      Avengers Assemble!     "
print("|" + s.lstrip(" \t\n\r\f") + "|")
print("|" + s.rstrip() + "|")  # trim \n from lines read from file
print("|" + s.strip() + "|")
print("s is still", repr(s))
print()
x = "foo\n\t\tbar\nblah\t"
print(x)
print(repr(x))
print()

s = "ggvvrrgggvvvrrrgAvengers Assemblervggggggggggggggvvvrrrrrr"
print("|" + s.lstrip("gvr") + "|")
print("|" + s.rstrip("gvr") + "|")  # trim \n from lines read from file
print("|" + s.strip("gvr") + "|")
print()
n = "00000323"
print(n.lstrip("0"))






