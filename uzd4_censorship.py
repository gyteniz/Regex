

"""'''Parašykite funkciją, kuri į parametrus priimtų tekstą ir žodžių, kuriuos reikia
jame išcenzūruoti sąrašą. Pvz, žodis "kvaraba" yra baisus keiksmažodis,
ir mums reikia duotame tekste pakeisti k*****a. Pradėkite maždaug taip:
# def cenzura(tekstas, *keiksmai):
    # čia bus jūsų funkcija

# iškvietus funkciją, pvz.:
# cenzura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')
# mums atspausdintų
# baisūs žodžiai, tokie kaip k*****a, ž****s..
žodžių cenzūravimui naudokite regex, o jų sukeitimui tekste naudokite .replace()\'''"""

import re


def censura(tekstas, *keiksmai):
    pattern = re.compile(r'([a-ząčęėįšųūž])([a-ząčęėįšųūž]+)([a-ząčęėįšųūž])')
    for zodis in keiksmai:
        grouped = pattern.search(zodis)
        censored_part = len(grouped.group(2)) * '*'
        censored_zodis = pattern.sub(f'\g<1>{censored_part}\g<3>', zodis)
        tekstas = tekstas.replace(zodis, censored_zodis)
    print(tekstas)


censura('baisūs žodžiai, tokie kaip kvaraba, žaltys..', 'kvaraba', 'žaltys')