import random
import string 

# stringexample = 'abcdef'
# print(random.choice(string) + str(random.randint(1000,9999)) + random.choice(string)*2)

def random_string(length=8):
    char_set = string.ascii_letters
    return  str(random.randint(1000,9999)) + ''.join(random.choice(char_set)for _ in range(length)/2)

password = random_string()
print(password)