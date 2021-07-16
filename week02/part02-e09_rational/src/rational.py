#!/usr/bin/env python3

class Rational(object):
    """rational number class"""
    def __init__(self, num, denom):
        "This initialises an instance of type ClassName"
        self.numerator = num
        self.denominator = denom
    def __str__(self):
        return '%s/%s' % (self.numerator, self.denominator)
    def __mul__(a, b):
        """Multiply two rational numbers."""
        return Rational(a.numerator * b.numerator, a.denominator * b.denominator)
    def __truediv__(a, b):
        """Divide two rational numbers."""
        return Rational(a.numerator * b.denominator, a.denominator * b.numerator)
    def __add__(a, b):
        """Divide two rational numbers."""
        return Rational(a.numerator * b.denominator + b.numerator * a.denominator, a.denominator * b.denominator)
    def __sub__(a, b):
        """Divide two rational numbers."""
        return Rational(a.numerator * b.denominator - b.numerator * a.denominator, a.denominator * b.denominator)
    def __eq__(a, b):
        """Divide two rational numbers."""
        return a.numerator == b.numerator and a.denominator == b.denominator
    def __gt__(self,y):
        if self.numerator*y.denominator > self.denominator*y.numerator:
            return True
        else: 
            return False
    def __lt__(self,y):
        if self.numerator*y.denominator < self.denominator*y.numerator:
            return True
        else: 
            return False

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
