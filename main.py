from datetime import date, datetime, timedelta
from collections import defaultdict


def get_birthdays_per_week(users):
    result_dict = defaultdict(list)

    if not users:
        return result_dict

    current_date = date.today()
    interval = timedelta(days=7)

    for person in users:
        person_birthday = person['birthday']
        person_name = person['name']
        person_birthday_curr_year = person_birthday.replace(
            year=current_date.year + int(person_birthday.month == 1)
            )
        num_weekday_1 = person_birthday_curr_year.isoweekday()

        if current_date < person_birthday_curr_year and \
           current_date + interval > person_birthday_curr_year:
            if num_weekday_1 not in (6, 7):
                result_dict[
                    person_birthday_curr_year.strftime('%A')
                    ].append(person_name)
            else:
                result_dict['Monday'].append(person_name)

    users = result_dict.copy()
    return users


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
