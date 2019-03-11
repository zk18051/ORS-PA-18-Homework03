"""
===================   TASK 2   ====================
* Name: Valid Mobile Number In Montenegro
*
* Write a function `valid_mobile_number` that will
* return True if given string is valid mobile phone
* number in Montenegro. Consider that +382 code will
* not be passed.
*
* Phone number is valid if:
*
*  - Has 9 or 10 digits
*  - Begins with '06'
*  - Third digit has to be one of [3, 6, 7, 8, 9]
*  - Contains digits only
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def valid_mobile_number(phone_number):
    x = len(phone_number)
    allowed1 = ['0','2','1','3','4','5','6','7','8','9']
    allowed3 = ['3','6','7','8','9']
    if 9<=x<=10:
        if phone_number[0:1]=='06':
            if phone_number[2] in allowed3:
                 return 'Valid'
            else:
                return 'Invalid'
        else:
            return 'Invalid'
    else:
        return 'Invalid'



def main():

    number_to_test = "068327319"
    if valid_mobile_number(number_to_test):
        print('Phone number +382-6' + number_to_test[2:len(number_to_test)]+ ' is valid in Montenegro!')
    else:
        print('Phone number is invalid in Montenegro!')
main()

# Ne radi kada korisnik unosi stringove i ostale nepravilne forme.