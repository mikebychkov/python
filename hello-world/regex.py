
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


###

### regex101.com

### 

def search_by_pattern(string, string_pattern):
    pattern = re.compile(string_pattern) 
    match = pattern.search(string)
    print(match)
    if match:
        print(match.group())
        return True
    return False


s = "Search this ip address 192.168.1.0/24 inside this text please after 31.03.2025 and sent it to whatever@woohoo.com !"

ip_a_pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}" # r = raw string - no nead of escape characters
cidr_pattern = r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/[0-9]{1,2}" # r = raw string - no nead of escape characters
search_by_pattern(s, cidr_pattern)

email_pattern = r"[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]+"
search_by_pattern(s, email_pattern)


# password pattern - at least 8 chars, letters, numbers, @#$%

def validate_password(password):
    password_pattern = r"^[0-9A-Za-z@#$%]{8,}$"
    valid = search_by_pattern(password, password_pattern)
    valid = valid and search_by_pattern(password, r"[A-Z]+")
    valid = valid and search_by_pattern(password, r"[a-z]+")
    valid = valid and search_by_pattern(password, r"[0-9]+")
    valid = valid and search_by_pattern(password, r"[@#$%]+")
    if valid:
        print("Password is ok")
    else:
        print("Password invalid")

password = "qwas12#$"

validate_password(password)
