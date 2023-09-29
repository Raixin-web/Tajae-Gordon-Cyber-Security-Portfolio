import re


def check_digit(pwd: str) -> bool:
    return bool(re.search(r'[0-9]', pwd))


def check_uppercase(pwd: str) -> bool:
    return bool(re.search(r'[A-Z]', pwd))


def check_lowercase(pwd: str) -> bool:
    return bool(re.search(r'[a-z]', pwd))


def check_special_char(pwd: str) -> bool:
    return bool(re.search(r'[~!@#$%&^?]', pwd))


def check_white_space(pwd: str) -> bool:
    return bool(re.search(r'\s', pwd))


def check_length(pwd: str) -> bool:
    return True if 8<=len(pwd)<=12 else False
# if 8<=len(pwd)<=12:
#   return True
# else:
#   return False

pwd =  input(' Please create a password or your account: ')

if all([check_digit(pwd), check_uppercase(pwd), check_lowercase(pwd),
       check_special_char(pwd), not check_white_space(pwd), check_length(pwd)]):
    print(' Your password is strong, excellent job!' )
else:
    print(' Oh my!, that password you entered does not meet the requirements.\n'
          ' Please make note of what is required below and try again ')

    if not check_digit(pwd):
        print(' -Password must contain at least one digit [0-9]')

    if not check_uppercase(pwd):
        print(' -Password must contain at least one uppercase letter')

    if not check_lowercase(pwd):
        print(' -Password must contain at least one lowercase letter')

    if not check_special_char(pwd):
        print(' -Password must contain at least one special character or symbol')

    if check_white_space(pwd):
        print(' -Password must NOT contain any space')

    if not check_length(pwd):
        print(' -Password must contain at least 8 characters and at most 12 characters')













