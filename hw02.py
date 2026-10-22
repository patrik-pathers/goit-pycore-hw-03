import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Генерує відсортований набір унікальних випадкових чисел у заданому діапазоні.

    :param min: Мінімальне можливе число у наборі (не менше 1).
    :param max: Максимальне можливе число у наборі (не більше 1000).
    :param quantity: Кількість чисел, які потрібно вибрати.
    :return: Відсортований список унікальних випадкових чисел або пустий список,
             якщо параметри не відповідають обмеженням.
    """
    if (
        not all(isinstance(arg, int) and not isinstance(arg, bool) for arg in (min, max, quantity))
        or min < 1
        or max > 1000
        or min > max
        or quantity < 1
        or quantity > (max - min + 1)
    ):
        return []

    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)


if __name__ == "__main__":
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print("Ваші лотерейні числа:", lottery_numbers)
