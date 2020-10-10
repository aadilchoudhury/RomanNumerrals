def int_to_roman(input_number):
    result = ""

    while input_number >= 1000:
        result = result + "M"
        input_number = input_number - 1000

    while input_number >= 500:
        result = result + "D"
        input_number = input_number - 500

    while input_number >= 100:
        result = result + "C"
        input_number = input_number - 100

    while input_number >= 50:
        result = result + "L"
        input_number = input_number - 50

    while input_number >= 10:
        result = result + "X"
        input_number = input_number - 10

    while input_number >= 5:
        result = result + "V"
        input_number = input_number - 5

    while input_number >= 1:
        result = result + "I"
        input_number = input_number - 1

    return result
