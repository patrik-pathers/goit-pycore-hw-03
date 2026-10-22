from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    """
    Розраховує кількість днів між заданою датою і поточною датою.

    :param date: Рядок, що представляє дату у форматі 'РРРР-ММ-ДД'.
    :return: Ціле число — кількість днів від заданої дати до поточної
             (від'ємне, якщо задана дата пізніша за поточну), або None у разі помилки формату.
    """
    try:
        target_date = datetime.strptime(date, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        delta = current_date - target_date
        return delta.days
    except (ValueError, TypeError):
        print(f"Помилка: Неправильний формат дати '{date}'. Використовуйте формат 'РРРР-ММ-ДД'.")
        return None


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
    print(get_days_from_today("2030-01-01"))
