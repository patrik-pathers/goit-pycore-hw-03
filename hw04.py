from datetime import date, datetime, timedelta


def _get_birthday_for_year(birthday: date, year: int) -> date:
    """
    Повертає дату дня народження у вказаному році з урахуванням 29 лютого.
    """
    try:
        return birthday.replace(year=year)
    except ValueError:
        return date(year, 3, 1)


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    """
    Визначає список колег, яких потрібно привітати з днем народження
    протягом наступних 7 днів (включаючи поточний день). Якщо день народження
    припадає на вихідний, дата привітання переноситься на наступний понеділок.

    :param users: Список словників із ключами 'name' та 'birthday' ('рік.місяць.дата').
    :return: Список словників із ключами 'name' та 'congratulation_date' ('рік.місяць.дата').
    """
    today = datetime.today().date()
    upcoming_birthdays: list[dict[str, str]] = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = _get_birthday_for_year(birthday, today.year)

        if birthday_this_year < today:
            birthday_this_year = _get_birthday_for_year(birthday, today.year + 1)

        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= 7:
            congratulation_date = birthday_this_year
            weekday = congratulation_date.weekday()

            if weekday == 5:  # Субота
                congratulation_date += timedelta(days=2)
            elif weekday == 6:  # Неділя
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
            })

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
