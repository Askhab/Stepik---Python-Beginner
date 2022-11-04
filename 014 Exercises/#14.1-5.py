# function declaration
def get_shipping_cost(quantity):
    return 1000 + (quantity - 1) * 120


# reading inputs
n = int(input())

# function call
print(get_shipping_cost(n))
