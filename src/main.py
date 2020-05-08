# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    pass_len = (random.randint(8, 16))
    password = [' '] * pass_len
    while ' ' in password:
        empty_spaces = [x for x in range(len(password)) if password[x] == ' ']
        if len(empty_spaces) > 0:
            password[random.choice(empty_spaces)] = string.ascii_lowercase[random.randint(0,len(string.ascii_lowercase))-1]
        
        if len(empty_spaces) > 1:
            password[random.choice(empty_spaces)] = string.ascii_uppercase[random.randint(0,len(string.ascii_uppercase))-1]
        
        if len(empty_spaces) > 2:
            password[random.choice(empty_spaces)] = string.digits[random.randint(0,len(string.digits))-1]
        
        if len(empty_spaces) > 3:
            password[random.choice(empty_spaces)] = random.choice(SYMBOLS)
    
    password_str = ''.join(x for x in password)
    return password_str

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
    run()
