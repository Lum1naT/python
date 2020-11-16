from tika import parser # pip install tika
import re

raw = parser.from_file('SEZNAMXP.pdf')

content = raw['content']
content_array = content.split("\n")
result = []
txt = open("seznamXP.txt", "a")

for firma in content_array:
    match = re.match("\A[0-9]+", firma)

    if match:
        result.append(firma)
        txt.write(firma + "\n")


print(result)
