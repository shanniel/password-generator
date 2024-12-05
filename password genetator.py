import random
import string
def password_genarator(length: len = 10):
    alphabet = string.ascii_letters+string.digits+string.punctuation
    password = "".join(random.choice(alphabet)for i in range(length))
    return password
password = password_genarator()
print(f"the password is {password}")