
value = 90

# || or
# && and
# ! not

if value > 75:  # block statement
    print("kangaroo")
    print("platypus")
elif value > 50:  # else if
    print("kookaburra")
    print("quokka")
else:
    print("wallaby")
    print("wombat")

print("Done.")

# X is False if
# X == 0
# X is False
# X is None
# len(X) == 0

#   int DEBUG = 1;
#  char *color = DEBUG ? "Green" : "Purple";
#   A?B:C

DEBUG = True
color = "Green" if DEBUG else "Purple"

if DEBUG:
    color = "Green"
else:
    color = "Purple"

#  == != < > >= <= is

# and or not

if (value > 50) and (value < 75):
    print("Ow ow ow")

if 50 < value < 75:
    print("What does the fox say?")

name = "Robert"
if (value > 50) and ("Rob" in name):
    print("Ping ping ping")

if (value > 50) or ("Rob" in name):
    print("Pong pong pong")

if value:    #  if bool(value) == True
    print("ha ha ha")

x = 0

if value and x:   #  if bool(value and x) == True
    print("Nooooooo")

if x > 10:  
    print("uh uh")















