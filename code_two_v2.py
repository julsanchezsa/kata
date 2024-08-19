import random

def sorted_squares(nums, threshold):
    """
    Toma una lista de enteros ordenados en orden ascendente y devuelve una nueva lista
    con los cuadrados de los enteros originales también ordenados en orden ascendente.
    Si el número cuadrado está fuera del rango [0, threshold], se elimina de la lista de salida.
    
    Args:
        nums (list): Lista de enteros ordenados en orden ascendente.
        threshold (int): Umbral para el rango de salida.
    
    Returns:
        list: Lista de cuadrados ordenados en orden ascendente dentro del rango permitido.
    """
    left = 0
    right = len(nums) - 1
    squared_nums = []

    while left <= right:
        left_num = nums[left] ** 2
        right_num = nums[right] ** 2
    
        if left_num < right_num:
            if right_num < threshold:
                squared_nums.append(right_num)
            right -= 1
        else:
            if left_num < threshold:
                squared_nums.append(left_num)
            left += 1
    
    return squared_nums[::-1]
  
def generate_random_list(size, min_value, max_value):
    """
    Genera una lista aleatoria de enteros.
    
    Args:
        size (int): Tamaño de la lista.
        min_value (int): Valor mínimo de los enteros en la lista.
        max_value (int): Valor máximo de los enteros en la lista.
    
    Returns:
        list: Lista de enteros aleatorios.
    """
    random_list = [random.randint(min_value, max_value) for _ in range(size)]
    random_list.sort()
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
        min_value = int(input("Ingrese el valor mínimo de los números en la lista: "))
        max_value = int(input("Ingrese el valor máximo de los números en la lista: "))
        nums = generate_random_list(size, min_value, max_value)
        print("Lista generada:", nums)
    else:
        print("Opción no válida")
        return

    threshold = int(input("Ingrese el umbral (threshold): ") * 2)
    print("Umbral:", threshold)
    result = sorted_squares(nums, threshold)
    print("Lista de cuadrados ordenados dentro del rango permitido:", result)

if __name__ == "__main__":
    main()