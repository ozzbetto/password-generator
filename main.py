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
    password = "".join(random.sample(character_pool, length))
    
    return password

def main():
    print("Password Generator Program.")
    print("===========================")

    try:
        length = int(input('\nEnter the length of the password: '))
        password = generate_password(length)
        print(password)
    except ValueError:
        print("Por favor, ingresa un número válido.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
