import random

def filter_numbers(numbers, threshold):
    """
    Filtra los números eliminando los dígitos mayores o iguales al umbral.
    
    Args:
        numbers (list): Lista de números a filtrar.
        threshold (int): Umbral para comparar los dígitos.
    
    Returns:
        list: Lista de números filtrados.
    """
    filtered_numbers = []
    for number in numbers:
        filter_number = ''
        for digits in str(number):
            if int(digits) < threshold:
                filter_number += digits
        if filter_number:
            filtered_numbers.append(int(filter_number))
    return filtered_numbers

def reverse_numbers(lst):
    """
    Invierte el orden de los elementos en la lista.
    
    Args:
        lst (list): Lista de elementos a invertir.
    
    Returns:
        list: Lista de elementos en orden inverso.
    """
    # reversed_list = lst[::-1]
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

def generate_random_list(size):
    """
    Genera una lista aleatoria de números.
    
    Args:
        size (int): Tamaño de la lista.

    
    Returns:
        list: Lista de números aleatorios.
    """
    return [random.randint(1, 100) for _ in range(size)]

def main():
    print("Seleccione una opción:")
    print("1. Ingresar la lista manualmente")
    print("2. Generar una lista aleatoria")
    option = input("Ingrese el número de la opción deseada: ")

    if option == '1':
        numbers = input("Ingrese los números separados por comas: ")
        numbers = list(map(int, numbers.split(',')))
    elif option == '2':
        size = int(input("Ingrese el tamaño de la lista: "))
        numbers = generate_random_list(size)
        print("Lista generada:", numbers)
    else:
        print("Opción no válida")
        return

    threshold = int(input("Ingrese el umbral (threshold): "))

    filtered = filter_numbers(numbers, threshold)
    reversed_filtered = reverse_numbers(filtered)
    print("Lista filtrada e invertida:", reversed_filtered)

if __name__ == "__main__":
    main()
