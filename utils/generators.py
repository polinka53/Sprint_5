import random
import string
from datetime import datetime

def _rand_digits(n=3):
    return "".join(random.choice(string.digits) for _ in range(n))

def gen_email():
    
    return f"polina_pavl_1999_{_rand_digits()}@yandex.ru"

def gen_password(min_len: int = 6):
    base = string.ascii_letters + string.digits
    pw = "".join(random.choice(base) for _ in range(max(6, min_len)))
    
    return pw

def gen_name():
    return "Polina_" + datetime.now().strftime("%H%M%S")