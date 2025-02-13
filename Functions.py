# function = A block of reusable code
#            place () after the function name to invoke it
def display_invoice(username, ammount, due_date):
    print(f"Hello {username}")
    print(f"You bill of ${ammount:.2f} is due: {due_date}")
    print()


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


print(f"Add: {add(1, 2)}")
print(f"Subtract: {subtract(1, 2)}")
print(f"Multiply: {multiply(1, 2)}")
print(f"Divide: {divide(1, 2)}")
print()


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last


full_name = create_name("arga", "nata")

print(full_name)
