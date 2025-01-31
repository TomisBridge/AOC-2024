def base_to(base_10, new_base):
    quotient = base_10 // new_base
    remainder = base_10 % new_base
    if quotient == 0:
        return remainder
    return int(str(base_to(quotient, new_base)) + str(remainder))

def to_10(number, base):
    if number < 10:
        return number
    else:
        digit = [int(str(number)[0]), int(str(number)[1:])]
        return digit[0] * base ** (len(str(number)) - 1) + to_10(digit[1], base)
    
