import sys

for file_path in sys.argv[1:]:
    with open(file_path) as file_in:
        for i, raw_line in enumerate(file_in, 1):
            print(i, raw_line.rstrip())
