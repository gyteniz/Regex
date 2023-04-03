"""#1
parašykite funkciją, kuri įvestą datą (formatas dd.mm.yyyy) keistų į yyyy mm dd.
Dėl datų logikos nesirūpinkite, dirbame grynai su tekstu."""

from datetime import datetime
import re

y = datetime.today()
print(y)
data = y.strftime("%d.%m.%Y %I:%M") #28.03.2023 03:05
print(data)
# data = "28.03.2023 03:05 viename laike"
print(type(data))

# pattern = re.compile(r'(\d{2})\.(\d{2})\.(\d{4})')
#
# res = pattern.search(data)
# print(res)
# print(res.group(3))


# pattern = re.compile(r'(\d{2})\.(\d{2})\.(\d{4})')
# res = pattern.search(data)
# print(res)

def date_format(date):
    pattern = re.compile(r'(\d{2})\.(\d{2})\.(\d{4})')
    res = pattern.sub(
        '\g<3> \g<2> \g<1>', date)

    return res

print(date_format(data))