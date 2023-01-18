import secrets
import string


# Con string, declaramos variables para letras, numeros y caracteres especiales

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = string.digits
special_chars = string.punctuation

chars = uppercase_letters + digits + lowercase_letters + special_chars

print("**********GENERADOR DE CONTRASEÑA**********")
print("-------------------------------------------")

# Cantidad de caracteres de la contraseña
pwd_lengh = int(input("Inserte la cantidad de caracteres: "))
# Cantidad de cantidad de contraseñas a generar
pwd_amount = int(input("Inserte la cuantas contrasenas quiere generar: "))


for i in range(pwd_amount):
    password = ''
    for x in range(pwd_lengh):
        password += ''.join(secrets.choice(chars))
    print("Contraseña " + password)
