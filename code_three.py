import random

def minimum_change(coins):
    """
    Dada una lista de enteros positivos que representan los valores de las monedas en tu posesión,
    devuelve la cantidad mínima de cambio (la suma mínima de dinero) que NO puedes dar como cambio.
    
    Args:
        coins (list): Lista de enteros positivos que representan los valores de las monedas.
    
    Returns:
        int: La cantidad mínima de cambio que no se puede crear.
    """
    coins.sort()
    change = 0
    
    for coin in coins:
        if coin > change + 1:
            break
        change += coin
    
    return change + 1


def generate_random_list(size, max_value):
    """
    Genera una lista aleatoria de enteros.
    
    Args:
        size (int): Tamaño de la lista.
        max_value (int): Valor máximo de los enteros en la lista.
    
    Returns:
        list: Lista de enteros aleatorios.
    """
    random_list = [random.randint(1, max_value) for _ in range(size)]
    return random_list


def main():
    print("Seleccione una opción:")
    print("1. Ingresar la lista manualmente")
    print("2. Generar una lista aleatoria")
    option = input("Ingrese el número de la opción deseada: ")

    if option == '1':
        numbers = input("Ingrese los números separados por comas: ")
        nums = list(map(int, numbers.split(',')))
    elif option == '2':
        size = int(input("Ingrese el tamaño de la lista: "))
        max_value = int(input("Ingrese el valor máximo de los números en la lista: "))
        nums = generate_random_list(size, max_value)
        print("Lista generada:", nums)
    else:
        print("Opción no válida")
        return

    result = minimum_change(nums)
    print("El cambio mínimo es:", result)

if __name__ == "__main__":
    main()

