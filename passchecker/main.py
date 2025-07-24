from typeguard import typechecked
import requests
import hashlib
import sys

@typechecked
def sha1_hash(text: str) -> str:
    sha1 = hashlib.sha1(text.encode('utf-8'))
    return sha1.hexdigest().upper()

passwd = sys.argv[1]

hash = sha1_hash(passwd)

first5, tail = hash[:5], hash[5:]

url = 'https://api.pwnedpasswords.com/range/' + first5

res = requests.get(url)

print(res)

for sh in res.iter_lines():
    shs = sh.decode()
    chstr = shs.split(':')[0]
    if chstr == tail:
        print('RESULT:\n', shs)

# not_str = 123
# print(sha1_hash(not_str)) # TypeCheckError
