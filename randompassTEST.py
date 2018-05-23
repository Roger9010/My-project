import random
import string
password = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(5))

print (password)