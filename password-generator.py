import random
import math
with open ('/usr/share/dict/words') as f:
    dictionary = f.read()
    f.close()
words = dictionary.split()
password = ''
for a in range(4):
    word = ''
    word = random.choice([word for word in words if len(word) >= 4 and len(word) <= 6])
    word = word.replace("'s", '').title()
    password += word
password = password[:-1]
password += str(random.randint(10,100))
print(password)
