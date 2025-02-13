# function = A block of reusable code
#            place () after the function name to invoke it
def display_invoice(username, ammount, due_date):
    print(f"Hello {username}")
    print(f"You bill of ${ammount:.2f} is due: {due_date}")


display_invoice("Arganata", 42.50, "01/01")


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


print(add(1, 2))
