"""Iš šio teksto atspausdinkite datų sąrašą."""


text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

import re

pattern = re.compile(r'([A-Z]\w+\s\d{1,2},\s20\d{2})')
result = pattern.findall(text)
print(result)



