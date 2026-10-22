import re


def normalize_phone(phone_number: str) -> str:
    """
    Нормалізує телефонний номер до стандартного формату (+380XXXXXXXXX),
    залишаючи тільки цифри та символ '+' на початку.

    :param phone_number: Рядок з телефонним номером у будь-якому форматі.
    :return: Нормалізований телефонний номер у вигляді рядка.
    """
    cleaned_number = re.sub(r"[^\d+]", "", phone_number.strip())

    if cleaned_number.startswith("+"):
        cleaned_number = "+" + re.sub(r"\D", "", cleaned_number)
        if cleaned_number.startswith("+380"):
            return cleaned_number
        if cleaned_number.startswith("+0"):
            return "+38" + cleaned_number[1:]
        return cleaned_number

    cleaned_number = re.sub(r"\D", "", cleaned_number)
    if cleaned_number.startswith("380"):
        return "+" + cleaned_number
    return "+38" + cleaned_number


if __name__ == "__main__":
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
