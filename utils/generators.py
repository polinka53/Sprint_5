import random
import string
from datetime import datetime

def _rand_digits(n=3):
    return ''.join(random.choice(string.digits) for _ in range(n))

def gen_email():
    """
    Генерирует уникальный e-mail в формате:
    polinapavl3355_XXX@yandex.ru  (XXX — случайные цифры)
    """
    suffix = _rand_digits(3)
    return f"polinapavl3355_{suffix}@yandex.ru"

def gen_password(min_len=6):
    """
    Пароль >= min_len, добавляем символы разных классов для надёжности.
    """
    alphabet = string.ascii_letters + string.digits
    core = ''.join(random.choice(alphabet) for _ in range(max(6, min_len)))
    return core + "A1"

def gen_name():
    """
    Простое уникальное имя на основе времени.
    """
    return "Polina_" + datetime.now().strftime("%H%M%S")
