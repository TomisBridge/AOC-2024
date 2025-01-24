def base_to(base_10, new_base):
    quotient = base_10 // new_base
    remainder = base_10 % new_base
    if quotient == 0:
        return remainder
    return int(str(base_to(quotient, new_base)) + str(remainder))
