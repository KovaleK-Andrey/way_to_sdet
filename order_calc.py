product_name = input('Введите название приобретаемого товара: ').capitalize()
price_per_unit = float(input('Введите цену за единицу товара: '))
product_quantity = int(input('Введите количество товара: '))
amount_without_discount = price_per_unit * product_quantity


if amount_without_discount > 5000:
    discount = 10
    print(f'Вы купили: {product_name}')
    print(f'Цена за шт: {price_per_unit:.0f}')
    print(f'Количество: {product_quantity}')
    print(f'Промежуточная сумма: {amount_without_discount:.0f}')
    print(f'Скидка: {discount}%')
    amount_with_discount = amount_without_discount - (amount_without_discount * (discount / 100))
    print(f'Итого к оплате: {amount_with_discount:.0f}')

elif 1000 < amount_without_discount < 5000:
    discount = 5
    print(f'Вы купили: {product_name}')
    print(f'Цена за шт: {price_per_unit:.0f}')
    print(f'Количество: {product_quantity}')
    print(f'Промежуточная сумма: {amount_without_discount:.0f}')
    print(f'Скидка: {discount}%')
    amount_with_discount = amount_without_discount - (amount_without_discount * (discount / 100))
    print(f'Итого к оплате: {amount_with_discount:.0f}')

else:
    discount = 0
    print(f'Вы купили: {product_name}')
    print(f'Цена за шт: {price_per_unit:.0f}')
    print(f'Количество: {product_quantity}')
    print(f'Промежуточная сумма: {amount_without_discount:.0f}')
    print(f'Скидка: {discount}%')
    amount_with_discount = amount_without_discount - (amount_without_discount * (discount / 100))
    print(f'Итого к оплате: {amount_with_discount:.0f}')
