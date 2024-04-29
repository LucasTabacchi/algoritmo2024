def roman_to_decimal(roman):

    roman = roman.upper()
    roman_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(roman) == 1 :
        return roman_numerals[roman]
    else:
        if len(roman) > 1 and roman_numerals[roman[0]] < roman_numerals[roman[1]]:
            return roman_to_decimal(roman[1:]) - roman_numerals[roman[0]]
        else:
            return roman_numerals[roman[0]] + roman_to_decimal(roman[1:])

roman_number = "mlv" 
print(roman_to_decimal(roman_number))