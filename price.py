def discounted(price, discount, max_discount=50):
    if max_discount > 99:
        raise ValueError('Максимальная скидка не может быть больше 100') 
    if discount >= max_discount:
        price_with_discount = price
    else:    
        price_with_discount = price - (price * discount / 100)
    return price_with_discount


product = {'name': 'Samsung Galaxy S10', 'stock':8, 'price':50000.0, 'discount':170}

product['with_second'] = discounted(product['price'], product['discount'], 170)

print(product['with_second'])

print()