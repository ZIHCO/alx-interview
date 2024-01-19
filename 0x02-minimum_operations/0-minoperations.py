#!/usr/bin/python3
"""contains the definition minOperations(n)"""


def minOperations(n):
    """returns the minimum number of time to perform
    a copy all and paste operations of the string 'H'"""

    if type(n) == int and n > 1:
        listOfMultiples = []
        for i in range(1, n + 1):
            if n % i == 0:
                listOfMultiples.append(i)
        numberOfH = "H"
        operations = ""
        for i in listOfMultiples:
            if i == 1:
                operations += "cp"
                numberOfH += "H"
                while len(numberOfH) < listOfMultiples[1]:
                    operations += "p"
                    numberOfH += "H"
                continue
            if len(numberOfH) == listOfMultiples[-1]:
                return len(operations)
            if i == listOfMultiples[1]:
                if listOfMultiples[2] % i != 0:
                    previousNumberOfH = numberOfH
                    operations += "cp"
                    numberOfH += numberOfH
                continue
            if i < len(numberOfH):
                continue
            if i % len(numberOfH) == 0:
                previousNumberOfH = numberOfH
                operations += "cp"
                numberOfH += numberOfH
                if i < len(numberOfH):
                    continue
                while len(numberOfH) < i:
                    operations += "p"
                    numberOfH += previousNumberOfH
                if len(numberOfH) == listOfMultiples[-1]:
                    return len(operations)
                continue

            previousNumberOfH = numberOfH
            operations += "cp"
            numberOfH += numberOfH
            while len(numberOfH) < listOfMultiples[-1]:
                operations += "p"
                numberOfH += previousNumberOfH
            if (n % 2) == 0:
                return len(operations) - 1
            return len(operations)
    return 0
