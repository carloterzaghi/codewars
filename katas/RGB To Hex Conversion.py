#Description:

# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"

# Link for Kata: https://www.codewars.com/kata/513e08acc600c94f01000001

# My code:

def rgb(r, g, b):
    lista = [i if i > 0 else 0 for i in [r, g, b]]
    return (
        f"{255 if lista[0] > 255 else lista[0]:02X}"
        f"{255 if lista[1] > 255 else lista[1]:02X}"
        f"{255 if lista[2] > 255 else lista[2]:02X}"
    )