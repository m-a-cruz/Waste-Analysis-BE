import random
import string

def generate_reset_token():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))