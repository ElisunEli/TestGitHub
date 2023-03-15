class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        #+
        new_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        #-
        new_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        #*
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        #/
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __pow__(self, other):
        #**

        if not isinstance(other, int):
            raise TypeError("Exponent must be an integer")
        if other == 0:
            return Fraction(1, 1)
        if other == 1:
            return Fraction(self.numerator, self.denominator)

        return Fraction(self.numerator ** other, self.denominator ** other)

    def __eq__(self, other):
        #==
        return self.numerator * other.denominator == self.denominator * other.numerator

    def __lt__(self, other):
        #<
        return self.numerator * other.denominator < self.denominator * other.numerator

    def __gt__(self, other):
        #>
        return self.numerator * other.denominator > self.denominator * other.numerator

    def __iadd__(self, other):
        #+=
        return self.__add__(other)

    def __isub__(self, other):
        #-=
        return self.__sub__(other)

    def __le__(self, other):
        #<=
        return self.numerator * other.denominator <= self.denominator * other.numerator

    def __ge__(self, other):
        #>=
        return self.numerator * other.denominator >= self.denominator * other.numerator

    def __ne__(self, other):
        #!=
        return not (self.numerator * other.denominator == self.denominator * other.numerator)

    def __imul__(self, other):
        #*=
        return self.__mul__(other)

    def __idiv__(self, other):
        #/=
        return self.__truediv__(other)

