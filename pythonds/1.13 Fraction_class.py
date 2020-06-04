# find the greatest common divisor (GCD)
# GCD = 𝑛 if 𝑛 divides 𝑚 evenly
# else GCD = greatest common divisor of 𝑛 and the remainder of 𝑚 divided by 𝑛. 
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn 
        n = oldm%oldn
        # print(oldm, oldn, m, n)
    return n
"""
A Fraction Class:
In Python, the constructor method is always called __init__ (two underscores before and after init)

class Fraction:
    def __init__(self, top, bottom):
        self.top = top
        self.den = bottom

self is a special parameter that will always be used as a reference back to the object itself. 
To create an instance of the Fraction class, we must invoke the constructor. This happens by using the name of the class and passing actual values for the necessary state (note that we never directly invoke __init__). For example,

    myfraction = Fraction(3,5)
    >>> print(myfraction)
    <__main__.Fraction instance at 0x40bce9ac>

creates an object called myfraction representing the fraction 3/5 (three-fifths).

The fraction object, myfraction, does not know how to respond to this request to print. The print function requires that the object convert itself into a string so that the string can be written to the output. 
"""

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)
    """
    >>> myf = Fraction(3,5)
    >>> print(myf)
    3/5
    >>> print("I ate", myf, "of the pizza")
    I ate 3/5 of the pizza
    >>> myf.__str__()
    '3/5'
    >>> str(myf)
    '3/5'
    >>>
    """
    # add "+" function:

    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newden, newnum)
        return Fraction(newnum//common, newden//common)
    """
    >>> f1=Fraction(1,4)
    >>> f2=Fraction(1,2)
    >>> f3=f1+f2
    >>> print(f3)
    6/8
    shollow equality: f1==f2 if they are references to the same object
    deep equality: two different objects with same values
    """
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

if __name__ == '__main__':
    x = Fraction(1,2)
    y = Fraction(2,3)
    print(x+y)
    print(x == y)


