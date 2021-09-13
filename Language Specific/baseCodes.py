# Given the four base codes of DNA: A, C, T, G
# Write a Python generator that can produces all possible sequences

# e.g. 'A', 'C', 'T', 'G', 'AA', 'AC', 'AT', etc
# islice(our_generator, 5, 7) = ['AC', 'AT']

from itertools import islice, product

def base_codes():
    base_codes = 'ACTG'
    i = 1
    while True:
        yield from ("".join(tup) for tup in product(base_codes, repeat=i))
        i += 1

def base_codes_alt_iterative():
    base_codes = ["A", "C", "T", "G"]
    combo_codes = []
    i = 0
    j = -1
    while True:
        prefix = combo_codes[j] if j >= 0 else ""
        combo = prefix + base_codes[i % 4]
        combo_codes.append(combo)
        yield combo
        i += 1
        if i % 4 == 0:
            j += 1

print(list(islice(base_codes_alt_iterative(), 100)))