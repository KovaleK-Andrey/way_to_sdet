from validators import validate_phone


test_data = {
    "+7 (999) 123-45-67": "79991234567",
    "8 999 123 45 67": "79991234567",
    "7 999 123 45 6": "Должно быть 11 цифр",
    "abc": "Номер должен содержать только цифры",
    "": "Номер пустой"
}

for phone, expected in test_data.items():
    result = validate_phone(phone)

    if result == expected:
        status = 'PASS'
    else:
        status = 'FAIL'

    print('INPUT:', phone)
    print('EXPECTED:', expected)
    print('ACTUAL:', result)
    print('RESULT:', status)
    print('-' * 30)