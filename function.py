def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum


calc_sum(5, 10)
calc_sum(20, 30)


def calc_product(a, b):
    product = a * b
    print(product)
    return product


calc_product(5, 10)
calc_product(20, 30)
calc_sum(calc_product(5, 10), calc_product(20, 30))
