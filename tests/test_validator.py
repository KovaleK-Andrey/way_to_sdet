import pytest
from validators import validate_phone, PhoneValidationError


@pytest.fixture(params=[
    ("89261234567", "79261234567"),  # Корректный российский номер (8)
    ("+79261234567", "79261234567"),  # Корректный российский номер (+7)
    ("79261234567", "79261234567"),   # Корректный российский номер (7)
    (" 8 (926) 123-45-67 ", "79261234567"),  # Корректный с форматированием
])
def valid_phone(request):
    return request.param


@pytest.fixture(params=[
    ("", "Номер пустой"),  # Пустая строка
    ("   ", "Номер пустой"),  # Строка из пробелов
    (None, "Номер пустой"), # None
    ("123", "Должно быть 11 цифр"),  # Слишком короткий
    ("8926123456", "Должно быть 11 цифр"), # короткий с 8
    ("+7926123456", "Должно быть 11 цифр"), # Короткий с +7
    ("7926123456", "Должно быть 11 цифр"), # короткий с 7
    ("8926123456789", "Должно быть 11 цифр"),  # Слишком длинный
    ("+7926123456789", "Должно быть 11 цифр"),  # Слишком длинный
    ("7926123456789", "Должно быть 11 цифр"),  # Слишком длинный
    ("abc123def45", "Номер должен содержать только цифры"),  # Номер должен содержать только цифры
])
def invalid_phone(request):
    return request.param


def test_validate_phone_valid_cases(valid_phone):
    phone, expected = valid_phone
    assert validate_phone(phone) == expected


def test_validate_phone_no_valid_cases(invalid_phone):
    phone, expected = invalid_phone

    with pytest.raises(PhoneValidationError) as exc:
        validate_phone(phone)
    assert str(exc.value) == expected