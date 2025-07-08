
import re

file_name = ""

### READ + RegEx

def extract_basic_auth_tokens(log_file_path):

    rsl = set()
    
    pattern = re.compile(r'Basic\s+([A-Za-z0-9+/=]+)')

    with open(log_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            match = pattern.search(line)
            if match:
                token = match.group(0).strip()
                rsl.add(token)

    return rsl

##

file = open(file_name, "r")
file.read()
file.readline()
file.readlines()


### WRITE

file = open(file_name, "w")
file = open(file_name, "r+") # read+write
file = open(file_name, "a") # append mode

file.write("qwas")


### WORKING WITH PATH'S

from pathlib import Path


