class Hw1Q2():
    """Attributes are coeffients for a monomial or polynomial"""
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def monomial(self):
        """User is prompted for integer inputs for a, b, and c if none exist...
        Method returns solution for ax - 2b = c"""
        if self.a == None or self.b == None or self.c == None:      # get user inputs
            self.a = int(input("Please enter an integer for a: "))
            self.b = int(input("Please enter an integer for b: "))
            self.c = int(input("Please enter an integer for c: "))
        x = (self.c + 2*self.b)/self.a                              # solve for x
        return print("\nFor the monomial %dx - 2*%d = %d, x = %d\n" % (self.a, self.b, self.c, x))

    def polynomial(self):
        """User is prompted for integer inputs for a, b, and c if none exist...
        Method returns solution for sqrt(ax + 2b) = c"""
        if self.a == None or self.b == None or self.c == None:      # get user inputs
            self.a = int(input("Please enter an integer for a: "))
            self.b = int(input("Please enter an integer for b: "))
            self.c = int(input("Please enter an integer for c: "))
        x = (self.c**2 - 2*self.b)/self.a                           # solve for x
        return print("\nFor the polynomial sqrt(%dx + 2*%d) = %d, x = %d\n" % (self.a, self.b, self.c, x))


if __name__ == '__main__':
    xMono = Hw1Q2()
    Hw1Q2.monomial(xMono)
    xPoly = Hw1Q2()
    Hw1Q2.polynomial(xPoly)
