import random
import string


def get_random_password(char_num=10):
    set_symbols = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    return ''.join([random.choice(list(set_symbols)) for _ in range(char_num)])


def get_random_email(char_num=5, server_name="@gmail.com"):
    random_email = (''.join(random.choice(string.ascii_lowercase) for _ in range(char_num)) + server_name)
    return random_email

