import re

myre = re.compile('a+b+')

examples = ['ab', 'aab', 'abb', 'aaabbb', 'ca', 'abab']

for e in examples:
    if myre.match(e):
        ismatch = True
    else:
        ismatch = False
    print(f"{e} -> {ismatch}")