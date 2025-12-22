

class AccessError(Exception):
    pass


def access_to_system(role: str, experience: str, has_pass: str):
    role = role.strip().lower()
    has_pass = has_pass.strip().lower()

    if not role:
        raise AccessError('Роль должна быть заполнена')
    if not experience.strip():
        raise AccessError('Опыт должен быть заполнен')

    try:
        experience = int(experience)
    except ValueError:
        raise AccessError('Опыт должен быть числом')

    if experience < 0:
        raise AccessError('Опыт не может быть отрицательным')

    allowed_roles = ['intern', 'employee', 'manager', 'admin']
    allowed_pass = ['yes', 'no']

    if role not in allowed_roles:
        raise AccessError('Незнакомая роль')
    if has_pass not in allowed_pass:
        raise AccessError('Недопустимый ответ')

    if has_pass == 'no':
        raise AccessError('Доступ запрещён: нет пропуска')

    if role == 'intern':
        raise AccessError('Доступ запрещён: стажёр не имеет доступа')
    if role == 'employee' and experience < 1:
        raise AccessError('Доступ запрещён: сотруднику требуется минимум 1 год опыта')
    if role == 'manager' and experience < 2:
        raise AccessError('Доступ запрещён: менеджеру требуется стаж от 2 лет')
    if role == 'admin':
        return f'Доступ разрешён {role}'

    return 'Доступ разрешён'