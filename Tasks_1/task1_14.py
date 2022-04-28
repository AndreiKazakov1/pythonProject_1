# Для целого числа К от 1 до 9 напечатать фразу «мне К лет», учитывая
# при этом, что при некоторых значениях К слово «лет» надо заменить
# на слово «год» или «года».

import numpy as np

num = np.random.randint(1, 9)
years = ''
if num == 1:
    years = 'год'
elif num == 2 or num == 3 or num == 4:
    years = 'года'
else:
    years = 'лет'
print(f'мне {num} {years}')
