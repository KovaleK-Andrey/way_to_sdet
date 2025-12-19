import pytest
from access import access_to_system


@pytest.mark.parametrize(
    'role, experience, has_pass, expected',
    [('manager', '1', 'no', 'Доступ запрещён: нет пропуска'),
    ('manager', '', 'yes', 'Опыт должен быть заполнен'),
    ('admin', '0', 'yes', 'Доступ разрешён: администратор'),
    ]
)


def test_access_to_system(role, experience, has_pass, expected):
    assert access_to_system(role, experience, has_pass) == expected