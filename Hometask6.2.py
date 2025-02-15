number = int(input("Enter the number: "))

if 0 <= number < 8640000:
    days, left_1 = divmod(number, 24 * 60 * 60)
    hours, left_2 = divmod(left_1, 60 * 60)
    minutes, seconds = divmod(left_2, 60)

    if days % 10 == 1 and days % 100 != 11:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
        day_word = "дні"
    else:
        day_word = "днів"

    print(f'{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}')
else:
    print("Enter the number of seconds only between 0 and 8640000.")
