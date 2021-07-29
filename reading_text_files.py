# file_obj = open("file_name")
# # read file here
# file_obj.close()
FILE_PATH = 'DATA/mary.txt'

# one line at a time
with open(FILE_PATH) as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n
        print(line)
print('-' * 60)

# read file into single str
with open(FILE_PATH) as mary_in:
    contents = mary_in.read()
    print("raw:")
    print(repr(contents))
    print("normal:")
    print(contents)
print('-' * 60)

# read file into list of str (with \n)
with open(FILE_PATH) as mary_in:
    lines_with_nl = mary_in.readlines()
    print(lines_with_nl)
print('-' * 60)

# read file into list of str (without \n)
with open(FILE_PATH) as mary_in:
    lines_without_nl = mary_in.read().splitlines()
    print(lines_without_nl)
print('-' * 60)

FIRST_LETTER = 'y'
FILE_PATH = 'DATA/words.txt'

count = 0
with open(FILE_PATH) as words_in:
    for line in words_in:
        if line.startswith(FIRST_LETTER):
            count += 1
print(f"{count} words start with {FIRST_LETTER}")


count = 0
with open('DATA/parrot.txt') as parrot_in:
    for raw_line in parrot_in:
        if "bird" in raw_line:
            line = raw_line.rstrip()
            count += 1
print(f"{count} lines contain 'bird'")



