user_role = input('Введите вашу роль: ').lower()
user_experience = int(input('Введите ваш стаж: '))
user_has_pass = input('Есть ли у вас пропуск? ').lower()


if user_has_pass == 'no':
    print('Доступ запрещён: нет пропуска')
elif user_role == 'intern':
    print('Доступ запрещён: стажёр не имеет доступа')
elif user_role == 'employee' and user_experience < 1:
    print('Доступ запрещён: сотруднику требуется минимум 1 год опыта')
elif user_role == 'manager' and user_experience < 2:
    print('Доступ запрещён: менеджеру требуется стаж от 2 лет')
elif user_role == 'admin':
    print('Доступ разрешён: администратор')
else:
    print('Доступ разрешён')
