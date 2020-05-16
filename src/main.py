# Resolve the problem!!
import string
import random

import unittest

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')

def generate_password():
    pass_len = random.randint(8, 16)
    password = [' '] * pass_len
    while ' ' in password:
        empty_spaces = gen_empty_spaces(password)
        if len(empty_spaces) > 0:
            password[random.choice(empty_spaces)] = string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase))-1]
        
        empty_spaces = gen_empty_spaces(password)
        if len(empty_spaces) > 0:
            password[random.choice(empty_spaces)] = string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase))-1]
        
        empty_spaces = gen_empty_spaces(password)
        if len(empty_spaces) > 0:
            password[random.choice(empty_spaces)] = string.digits[random.randint(0,len(string.digits))-1]
        
        empty_spaces = gen_empty_spaces(password)
        if len(empty_spaces) > 0:
            password[random.choice(empty_spaces)] = random.choice(SYMBOLS)
    
    password_str = ''.join(password)
    return password_str

def gen_empty_spaces(password):
    return [x for x in range(len(password)) if password[x] == ' ']

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    class passTest(unittest.TestCase):
        def test_secure_pass(self):
            for i in range(1000):
                self.assertEqual(True, validate(generate_password()))

    #unittest.main()
    run()
