

def validate_phone(phone: str):

    if not phone:
        return 'Номер пустой'

    clean_phone = (phone.strip()
                   .replace('+', '')
                   .replace(' ', '')
                   .replace('(', '')
                   .replace(')', '')
                   .replace('-', ''))

    if clean_phone[0] == '8':
        clean_phone = clean_phone.replace('8', '7', 1)

    if not clean_phone.isdigit():
        return 'Номер должен содержать только цифры'
    elif len(clean_phone) != 11:
        return 'Должно быть 11 цифр'
    elif clean_phone[0] != '7':
        return 'Номер должен начинаться с 7'
    else:
        return f'Номер корректный: {clean_phone}'
