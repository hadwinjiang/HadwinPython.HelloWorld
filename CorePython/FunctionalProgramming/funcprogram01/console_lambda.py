scientists = ['Marie Curie', 'Albert Einstein', 'Rosalind Franklin',
              'Niels Bohr', 'Dian Fossey', 'Isaac Newton',
              'Grace Hopper', 'Charles Darwin', 'Lise Meitner']

sorted(scientists, key=lambda name: name.split()[-1])

last_name = lambda name: name.split()[-1]

last_name
last_name("Nikola Tesla")