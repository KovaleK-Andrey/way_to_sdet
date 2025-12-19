import pytest
from validators import validate_phone


@pytest.mark.parametrize(
    'phone, expected',
    [
        ('+7 (999) 123-45-67', '79991234567'),
        ('8 999 123 45 67', '79991234567'),
        ('7 999 123 45 6', 'Должно быть 11 цифр'),
        ('abc', 'Номер должен содержать только цифры'),
        ('', 'Номер пустой'),
    ]
)


def test_validate_phone(phone, expected):
    assert validate_phone(phone) == expected