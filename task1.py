"""
===================   TASK 1   ====================
* Name: Sum Number Digits
*
* Write a function `sum_digits` that will return
* sum of digits for given integer number.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def sum_digits(number):
    allowed_character = ['0','2','1','3','4','5','6','7','8','9','-']
    for ch in str(number):
        if ch in allowed_character:
            pass
        else:
            return '-1'
    if int(number) <= 0:
        number1 = abs(int(number))
    else:
        pass

    sumdigit=0
    for digits in str(number1):
        sumdigit += int(digits)
    return sumdigit

def main():
    number = '123.4'
    digit_sum = sum_digits(number)
    print("Sum of digits for given numbers is: ", digit_sum)

main()

# Ne radi za situaciju kada su dati brojevi tipa float i kada minus nije na svom mjestu ('number[0]').