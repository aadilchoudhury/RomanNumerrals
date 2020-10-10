def int_to_roman(input_number):
    if input_number == 1:
        return "I"
    if input_number > 2:
        return "IV"

    return "V"
