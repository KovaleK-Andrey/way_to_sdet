from access import access_to_system


test_data_access = (('manager', '1', 'no', 'Доступ запрещён: нет пропуска'),
                    ('manager', '', 'yes', 'Опыт должен быть заполнен'),
                    ('admin', '0', 'yes', 'Доступ разрешён: администратор'))

for role, experience, has_pass, expected in test_data_access:
    result = access_to_system(role, experience, has_pass)

    if result == expected:
        status = 'PASS'
    else:
        status = 'FAIL'

    print('ROLE:', role)
    print('EXPERIENCE:', experience)
    print('PASS:', has_pass)
    print('ACTUAL:', result)
    print('EXPECTED:', expected)
    print('RESULT:', status)
    print('-' * 30)