
## CHECK file_io.py FOR EXAMPLE

import re

pattern = re.compile("this")

s = "Search this inside this text please!"

match = pattern.search(s)
if match:
    print(match.group())

rsl = pattern.findall(s)
print(rsl)

match2 = pattern.match("this")
if match2:
    print(match2.group())
    print(match2.span())
    print(match2.start())
    print(match2.end())
else:
    print("No match")


### regex101.com
