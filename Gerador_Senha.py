import random
import string

def generate_password(length):
    aspec = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(aspec) for i in range(length))
    return senha

length = int(input("Quantos caracteres a senha deve ter? "))

senha = generate_password(length)
print(f"Sua nova senha é: {senha}")
