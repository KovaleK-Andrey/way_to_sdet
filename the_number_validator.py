phone = input('Введите номер телефона: ')
clean_phone = (phone.strip(' +')
             .replace(' ', '')
             .replace('(', '')
             .replace(')', '')
             .replace('-', ''))

if not clean_phone:
    print('Номер пустой')
elif clean_phone[0] == '8':
    clean_phone = clean_phone.replace('8', '7', 1)

if not clean_phone.isdigit():
    print('Номер должен содержать только цифры')
elif len(clean_phone) != 11:
    print('Должно быть 11 цифр')
elif clean_phone[0] != '7':
    print('Номер должен начинаться с 7')
else:
    print(f'Номер корректный: {clean_phone}')


