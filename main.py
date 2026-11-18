
import re

text = input()

pattern = r'(?<!\d)(?:(\d{4})-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])|(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/(\d{4}))(?!\d)'

matches = re.finditer(pattern, text)

found = False

for match in matches:
    if match.group(1):
        year = match.group(1)
        month = match.group(2)
        day = match.group(3)
    else:
        day = match.group(4)
        month = match.group(5)
        year = match.group(6)

    print(f"{year}-{month}-{day}")
    found = True

if not found:
    print("None")
