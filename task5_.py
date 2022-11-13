import random
import string

n=8
def get_random_password(n) -> str:

 s = string.ascii_uppercase + string.ascii_lowercase + "0123456789"
 return ''.join(random.sample(s, n))




print(get_random_password(n))
