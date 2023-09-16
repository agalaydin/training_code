"""Python in 7 hours."""

import os

sayt = input()

if 'https://' in sayt:
    os.system('start ' + sayt)
    print('if')

elif 'www.' in sayt:
    sayt = 'https://' + sayt
    os.system('start ' + sayt)
    print('elif')

else:
    sayt = 'https://www.' + sayt
    os.system('start ' + sayt)
    print('else')
    