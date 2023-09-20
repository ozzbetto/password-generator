import random
import string

def generate_password(length):
    """
    Genera una contraseña aleatoria de la longitud especificada.
    
    Args:
    length (int): La longitud de la contraseña a generar.

    Returns:
    str: Una cadena que representa la contraseña generada.
    """
    if length <= 0:
        return "La longitud de la contraseña debe ser mayor que cero"

    character_pool = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choices(character_pool, k=length))
    
    return password

def get_password_length():
    while True:
        try:
            length = int(input('\nIngrese la longitud de la contraseña: '))
            if length <= 0:
                raise ValueError("La longitud de la contraseña debe ser mayor que cero.")
            return length
        except ValueError as e:
            print(e)

def main():
    print("Password Generator Program.")
    print("===========================")

    try:
        length = get_password_length()
        password = generate_password(length)
        print(password)
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
