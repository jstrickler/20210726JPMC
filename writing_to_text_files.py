fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in fruits:
        fruits_out.write(fruit + '\n')  # "f{fruit}\n"

with open('DATA/words.txt') as words_in:
    with open('xwords.txt', 'w') as xwords_out:
        for line in words_in:
            if line.startswith('x'):
                xwords_out.write(line)
