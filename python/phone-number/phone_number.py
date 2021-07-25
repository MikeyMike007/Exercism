import string

class PhoneNumber:
    def __init__(self, number):
        """
        Set the phonenumber and area code according to right specification.
        """
        self.number = self.numberify(number)
        # Areacode is the first three numbers of the phonnumer in the right
        # format
        self.area_code = self.number[0:3]

    def numberify(self, number):
        """
        Check validity of the input number and delete country code if specified.
        Return all the digits in the phonenumber ex country code if valid.
        """
        digits = ''.join(digit for digit in number if digit in string.digits)
        if len(digits) == 11 and digits[0] == '1':
            digits = digits[1:]

        if len(digits) != 10:
            raise ValueError("Error: Phonenumber length is not valid")
        if digits[0] in ['0', '1']:
            raise ValueError("Error: Areacode is not valid")
        if digits[3] in ['0', '1']:
            raise ValueError("Error: Number not valid")

        return digits

    def pretty(self):
        """
        Returns phonenumber according to the pre-defined format: (XXX)-XXX-XXXX
        """

        # using f-string
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"

