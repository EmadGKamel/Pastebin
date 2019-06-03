import string
import random

def url_shortner():
    return ''.join(random.choice(string.hexdigits[:15]) for x in range(12))

#print(url_shortner())