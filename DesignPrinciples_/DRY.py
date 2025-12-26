def calculate_discount(price):
    return price * 0.1


def final_price(price):
    return price - calculate_discount(price)


def refund_amount(price):
    return calculate_discount(price)


print(final_price(1000))
print(refund_amount(1000))
