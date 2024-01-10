#შექმენით random password generator პროგრამა რომელშიც დაგენერირდბა პაროლი, 8 სიმბოლოიანი, სადაც აუცილებლად 2 სიმბოლო იქნება !##%(#)^#, 2 სიმბოლო იქნება აბგქწეკჯასკჯქწე , 4 სიმბოლო იქნება ციფრები 215346347347
# მაგ: !n8391k*

import random

def generate_random_password():
    symbols_set1 = "!##%(#)^#"
    symbols_set2 = "abcdefghijklmnopqrstuvwxyz"
    symbols_set3 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits_set = "215346347347"

    password = []

    password.append(random.choice(symbols_set1))
    password.append(random.choice(symbols_set1))

    password.append(random.choice(symbols_set2))
    password.append(random.choice(symbols_set2))

    password.append(random.choice(digits_set))
    password.append(random.choice(digits_set))
    password.append(random.choice(digits_set))
    password.append(random.choice(digits_set))

    random.shuffle(password)

    password_str = ''.join(password)

    return password_str

random_password = generate_random_password()
print(random_password)
