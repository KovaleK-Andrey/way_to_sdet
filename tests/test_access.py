import pytest
from access import access_to_system


@pytest.fixture(params=[
    ('manager', '1', 'no', 'Доступ запрещён: нет пропуска'),
    ('manager', '', 'yes', 'Опыт должен быть заполнен'),
    ('admin', '0', 'yes', 'Доступ разрешён: администратор'),
    ('intern', '10', 'yes', 'Доступ запрещён: стажёр не имеет доступа'),
])
def user_access_data(request):
    return request.param


def test_access_to_system(user_access_data):
    role, experience, has_pass, expected = user_access_data
    assert access_to_system(role, experience, has_pass) == expected