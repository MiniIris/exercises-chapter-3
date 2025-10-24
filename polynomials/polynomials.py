from numbers import Number
from numbers import Integral

class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs

    def degree(self):
        return len(self.coefficients) - 1

    def __str__(self):
        coefs = self.coefficients
        terms = []

        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")

        terms += [f"{'' if c == 1 else c}x^{d}"
                  for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"

    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"

    def __eq__(self, other):

        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
    
    def __sub__(self, other):

        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients,
                                                other.coefficients))
            coefs += self.coefficients[common:] + tuple(-c for c in other.coefficients[common:])

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,)
                              + self.coefficients[1:])

        else:
            return NotImplemented
        
    def __rsub__(self, other):
    
        if isinstance(other, Number):
            coefs = (other - self.coefficients[0],) + tuple(-c for c in self.coefficients[1:])
            return Polynomial(coefs)
        else:
            return NotImplemented
        

    from numbers import Number

    def __mul__(self, other):

        if isinstance(other, Polynomial):
            m, n = self.degree(), other.degree()
        
            result = [0] * (m + n + 1)

        
            for i, a in enumerate(self.coefficients):
                for j, b in enumerate(other.coefficients):
                    result[i + j] += a * b

            return Polynomial(tuple(result))

        elif isinstance(other, Number):
        
            return Polynomial(tuple(a * other for a in self.coefficients))

        else:
         return NotImplemented
        
    def __rmul__(self,other):
        if isinstance(other, Number):
            return Polynomial(tuple(other * b for b in self.coefficients))
            #...self*other
        else:
            return NotImplemented
        


    def __pow__(self, power):
   
        if not isinstance(power, Integral):
            return NotImplemented

   
        if power < 0:
            raise ValueError

    
        if power == 0:
        
            return Polynomial((1,))
    
   
        else:
            result = Polynomial((1,))     
            for _ in range(power):
                result = result * self    
            return result
    
    def __call__(self,x):
        if not isinstance(x,Number):
            return NotImplemented
        else:
            result=0
            for i,a in enumerate(self.coefficients):
                result+= a *(x**i)
            return result
    

    def dx(self):
        n = len(self.coefficients)
        if n <= 1:
             return Polynomial((0,))
        else:
            deriv = tuple(i * self.coefficients[i] for i in range(1, n))
            return Polynomial(deriv)



def derivative(p):
    if not isinstance(p, Polynomial):
        return NotImplemented
    return p.dx()