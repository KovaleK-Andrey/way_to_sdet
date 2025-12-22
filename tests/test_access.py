import pytest
from access import access_to_system, AccessError


@pytest.fixture(params=[
    ('admin', '10', 'no', 'Доступ запрещён: нет пропуска'),
    ('manager', '1', 'no', 'Доступ запрещён: нет пропуска'),
    ('manager', '', 'yes', 'Опыт должен быть заполнен'),
    ('intern', '10', 'yes', 'Доступ запрещён: стажёр не имеет доступа'),
    ('employee', '0', 'yes', 'Доступ запрещён: сотруднику требуется минимум 1 год опыта'),
    ('employee', '10', 'no', 'Доступ запрещён: нет пропуска'),
    ('  ', '10', 'yes', 'Роль должна быть заполнена'),  # Тест на пробел в роли
    ('manager', '-1', 'yes', 'Опыт не может быть отрицательным'),
])
def user_access_invalid_data(request):
    return request.param


@pytest.fixture(params=[
    ('manager', '2', 'yes', 'Доступ разрешён'),
    ('manager', '22', 'yes', 'Доступ разрешён'),
    ('admin', '0', 'yes', 'Доступ разрешён admin'),
    ('admin', '10', 'yes', 'Доступ разрешён admin'),
    ('employee', '1', 'yes', 'Доступ разрешён'),
    ('employee', '10', 'yes', 'Доступ разрешён'),
    ('  admin  ', ' 10 ', 'yes', 'Доступ разрешён admin'),  # Пробелы
    ('AdMiN', '10', 'yes', 'Доступ разрешён admin'),
])
def user_access_valid_data(request):
    return request.param


def test_access_to_system_invalid_data(user_access_invalid_data):
    role, experience, has_pass, expected = user_access_invalid_data

    with pytest.raises(AccessError) as exc:
        access_to_system(role, experience, has_pass)

    assert str(exc.value) == expected


def test_access_to_system_valid_data(user_access_valid_data):
    role, experience, has_pass, expected = user_access_valid_data

    assert access_to_system(role, experience, has_pass) == expected