"""Atspausdinkite tą patį teksta taip:
# 1.
# Event: Workshop & Tutorial proposals due
# Date: November 21, 2019

# 2.
# Event: Notification of acceptance
# Date: December 1, 2019

# ir t.t."""

text = '''Workshop & Tutorial proposals: November 21, 2019
Notification of acceptance: December 1, 2019
Workshop & Tutorial websites online: December 18, 2019
Workshop papers: February 28, 2020
Workshop paper notifications: March 27, 2020
Workshop paper camera-ready versions: April 10, 2020
Tutorial material due (online): April 10, 2020'''

import re

# pattern = re.compile(r'(^.+):\s([A-Z]\w+ \d{1,2}, 20\d{2})')
# pattern = re.compile(r'(^.+):(.+)$')
# nr=1
# for line in text.splitlines():
#     result = pattern.search(line)
#     print(f'{nr}.\nEvent: {result.group(1)}\nDate: {result.group(2)}\n')
#     nr += 1

pattern = re.compile(r'(^.+):\s(.+)$', re.MULTILINE)
res = pattern.findall(text)
print(res)

for nr, event in enumerate(res, 1):
    print(f"{nr}.")
    print("Event:", event[0])
    print("Date:", event[1])
    print()