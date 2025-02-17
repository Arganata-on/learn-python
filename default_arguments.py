# default arguments = A default value for certain parameters
#                     default is used when that argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary


def net_price(list_price, discount, tax):
    return list_price * (1 - discount) * (1 + tax)


print(net_price(500, 0, 0.05))
