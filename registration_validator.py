email = input('Введите ваш email: ')
password = input('Введите ваш пароль: ')
age = input('Введите ваш возраст: ')

error_email = ''

if len(email) < 5:
    error_email = 'Email должен быть не короче 5 символов'
elif '@' not in email or '.' not in email:
    error_email = 'Email должен содержать символы @ и .'
elif email[0] in '@.' or email[-1] in '@.':
    error_email = 'Email не должен начинаться или заканчиваться на @ или .'


error_password = ''

if len(password) < 8:
    error_password = 'Пароль должен быть длиной не менее 8 символов'
elif not any(c.isdigit() for c in password):
    error_password = 'Пароль должен содержать минимум одну цифру'
elif not any(c.isalpha() for c in password):
    error_password = 'Пароль должен содержать минимум одну букву'


error_age = ''

if not age.isdigit():
    error_age = 'Возраст должен быть числом'
elif int(age) < 18:
    error_age = 'Возраст должен быть 18 или больше'


if not error_email and not error_password and not error_age:
    print('Регистрация успешна!')
else:
    print('Ошибка:')
    if error_email:
        print('-', error_email)
    if error_password:
        print('-', error_password)
    if error_age:
        print('-', error_age)