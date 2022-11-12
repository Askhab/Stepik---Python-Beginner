def convert_number(number):
    print(bin(number)[2:])
    print(oct(number)[2:])
    print(hex(number).upper()[2:])


convert_number(int(input()))
