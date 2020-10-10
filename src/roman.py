def int_to_roman(input_number):
    result = ""

    while input_number >= 1000:
        result = result + "M"
        input_number = input_number - 1000

    if input_number >= 900:
            result = result + "CM"
            input_number = input_number - 900

    while input_number >= 500:
        result = result + "D"
        input_number = input_number - 500

    if input_number >= 400:
            result = result + "CD"
            input_number = input_number - 400

    while input_number >= 100:
        result = result + "C"
        input_number = input_number - 100

    if input_number >= 90:
            result = result + "XC"
            input_number = input_number - 90

    while input_number >= 50:
        result = result + "L"
        input_number = input_number - 50

    if input_number >= 40:
            result = result + "XL"
            input_number = input_number - 40

    while input_number >= 10:
        result = result + "X"
        input_number = input_number - 10

    if input_number >= 9:
            result = result + "IX"
            input_number = input_number - 9

    while input_number >= 5:
        result = result + "V"
        input_number = input_number - 5

    if input_number >= 4:
            result = result + "IV"
            input_number = input_number - 4

    while input_number >= 1:
        result = result + "I"
        input_number = input_number - 1

    return result
