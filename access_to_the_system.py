

def access_to_system(role: str, experience: int, has_pass: str):
    if not role:
        return 'Роль должна быть заполнена'
    if experience is None:
        return 'Опыт должен быть заполнен'

    role = role.strip().lower()
    has_pass = has_pass.strip().lower()

    allowed_roles = ['intern', 'employee', 'manager', 'admin']
    allowed_pass = ['yes', 'no']

    if role not in allowed_roles:
        return 'Незнакомая роль'
    if has_pass not in allowed_pass:
        return 'Недопустимый ответ'

    if has_pass == 'no':
        return 'Доступ запрещён: нет пропуска'

    if role == 'intern':
        return 'Доступ запрещён: стажёр не имеет доступа'
    if role == 'employee' and experience < 1:
        return 'Доступ запрещён: сотруднику требуется минимум 1 год опыта'
    if role == 'manager' and experience < 2:
        return 'Доступ запрещён: менеджеру требуется стаж от 2 лет'
    if role == 'admin':
        return 'Доступ разрешён: администратор'

    return 'Доступ разрешен'