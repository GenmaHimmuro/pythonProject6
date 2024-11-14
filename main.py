# Выполнял(а) урок на Windows, urwid не работает.
PASSWORD = print('Введите пароль:'),input()

def is_very_long(PASSWORD):
    return len(PASSWORD)>12

def has_digit(PASSWORD):
    return any(n.isdigit() for n in PASSWORD)

def has_letters(PASSWORD):
    return any(n.isalpha() for n in PASSWORD)

def has_upper_letters(PASSWORD):
    return any(n.isupper() for n in PASSWORD)

def has_lower_letters(PASSWORD):
    return any(n.islower() for n in PASSWORD)

def has_symbols(PASSWORD):
    return any(not n.isalnum() for n in PASSWORD)

def main():
    score_password = 0
    all_functions = [
        has_lower_letters,
        has_upper_letters,
        has_letters,
        has_digit,
        is_very_long,
        has_symbols
    ]
    for n in all_functions:
        if n:
            score_password +=2
    print(f'Рейтинг пароля - {score_password}')


if __name__ == "__main__":
     main()

