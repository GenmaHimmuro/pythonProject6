import urwid


def is_very_long(password):
    return len(password) > 12


def has_digit(password):
    return any(n.isdigit() for n in password)


def has_letters(password):
    return any(n.isalpha() for n in password)


def has_upper_letters(password):
    return any(n.isupper() for n in password)


def has_lower_letters(password):
    return any(n.islower() for n in password)


def has_symbols(password):
    return any(not n.isalnum() for n in password)


def score(edit, new_password):
    score_password = 0
    all_functions = [
        has_lower_letters,
        has_upper_letters,
        has_letters,
        has_digit,
        is_very_long,
        has_symbols
    ]
    for correct in all_functions:
        if correct(new_password):
            score_password+=2
    score_text.set_text(f'Рейтинг пароля: {score_password}')


def password():
    global score_text
    ask = urwid.Edit("Введите пароль: ", mask='*')
    score_text = urwid.Text("Рейтинг пароля: 0")
    menu = urwid.Pile([ask, score_text])
    menu = urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', score)
    urwid.MainLoop(menu).run()


if __name__ == '__main__':
    password()
