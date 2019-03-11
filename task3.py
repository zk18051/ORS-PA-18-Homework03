"""
===================   TASK 3   ====================
* Name:  Euclidean algorithm
*
* Write a function `gcd` that will calculate
* greatest common divisor for two integer values.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def qcd(x, y):
    x = abs(int(x))
    y = abs(int(y))
    if x > y:
        a = y
    else:
         a = x
    for i in range(1, a + 1):
        if (x % i == 0) and (y % i == 0):
            qcd = i

    return qcd
def main ():
    x = input('Enter a first integer number: ')
    y = input('Enter a secund integer number: ')
    division = qcd(x,y)
    print(division)

main()

# Ne radi za brojeve vrste float i za stringove.
