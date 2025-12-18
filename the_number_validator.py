

def validate_phone(phone: str):

    if not phone:
        return 'Номер пустой'

    clean_phone = (phone.strip()
                   .replace('+', '')
                   .replace(' ', '')
                   .replace('(', '')
                   .replace(')', '')
                   .replace('-', ''))

    if not clean_phone:
        return 'Номер пустой'

    if clean_phone[0] == '8':
        clean_phone = clean_phone.replace('8', '7', 1)

    if not clean_phone.isdigit():
        return 'Номер должен содержать только цифры'
    elif len(clean_phone) != 11:
        return 'Должно быть 11 цифр'
    elif clean_phone[0] != '7':
        return 'Номер должен начинаться с 7'
    else:
        return clean_phone


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