from datetime import datetime

#Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
def get_days_from_today(date):
    try:
#Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
        datetime_object = datetime.strptime(date,"%Y-%m-%d")
#Отримайте поточну дату, використовуючи datetime.today().
        current_datetime = datetime.today()
#Розрахуйте різницю між поточною датою та заданою датою.
        difference_in_time = current_datetime.toordinal() - datetime_object.toordinal()
#Поверніть різницю у днях як ціле число.
        return difference_in_time
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

print(get_days_from_today("2024-12-05"))

