# return = statement used to end a function
#          and send a result back to the caller


def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def multiply(x, y):
    z = x * y
    return z


def divide(x, y):
    z = x / y
    return z


print(f"Penjumlahan: {add(1, 2)}")
print(f"Pengurangan: {subtract(1, 2)}")
print(f"Perkalian: {multiply(1, 2)}")
print(f"Pembagian: {divide(1, 2)}")
