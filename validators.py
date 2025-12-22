

class PhoneValidationError(Exception):
    pass


def validate_phone(phone: str):

    if not phone:
        raise PhoneValidationError('Номер пустой')

    clean_phone = (phone.strip()
                   .replace('+', '')
                   .replace(' ', '')
                   .replace('(', '')
                   .replace(')', '')
                   .replace('-', ''))

    if not clean_phone:
        raise PhoneValidationError('Номер пустой')

    if clean_phone[0] == '8':
        clean_phone = '7' + clean_phone[1:]

    if not clean_phone.isdigit():
        raise PhoneValidationError('Номер должен содержать только цифры')
    elif len(clean_phone) != 11:
        raise PhoneValidationError('Должно быть 11 цифр')
    elif clean_phone[0] != '7':
        raise PhoneValidationError('Номер должен начинаться с 7')
    else:
        return clean_phone