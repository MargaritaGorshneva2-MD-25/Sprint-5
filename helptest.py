import random
import string


def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "mail.ru", "outlook.com"]
    username_length = 10
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for i in range(username_length))
    domain = random.choice(domains)
    return f"{username}@{domain}"
