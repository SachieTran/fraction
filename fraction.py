# fraction.py
#
# Created by: Tran Tran
# Date: 3/1/2016
#
# This program contains the Fraction ADT that represents a rational number that
# consists of two integer values: one for the denominator and one for the
# numerator.

class Fraction :
   # Creates a new rational number from the supplied values. The denominator
   # can not be zero.   
   def __init__(self, num, den) :
      assert den != 0, "The denominator can not be zero."
      if num == 0 :
         self._numerator = num
         self._denominator = 1
      else :
         # Find the greatest common divisor (gcd) of the numerator and 
         # denominator.
         a = num
         b = den
         gcd = den
         while (a % b) != 0 :
            tmpA = a
            tmpB = b
            a = tmpB
            b = tmpA % tmpB      
            gcd = b 
         self._numerator = int(num / gcd)
         self._denominator = int(den / gcd)        
      
   # Returns the numerator part of the rational number.   
   def getNum(self) :
      return self._numerator
   
   # Returns the denominator part of the rational number.
   def getDen(self) :
      return self._denominator
   
   #  Returns a Boolean indicating if the rational number is zero.
   def isZero(self) :
      if self._numerator == 0 :
         return True
      else :
         return False
      
   # Returns a Boolean indicating if the rational number is negative.
   def isNegative(self) :
      if self._numerator < 0 and self._denominator < 0 :
         return False
      elif self._numerator > 0 and self._denominator > 0 :
         return False
      else :
         return True
   
   # Returns a new rational number that is the reciprocal of this rational
   # number.
   def reciprocal(self) :
      if self._numerator == 0 :
         reciprocal = Fraction(0, 1)
      else :
         reciprocal = Fraction(self._denominator, self._numerator)   
      return reciprocal
   
   # Returns the floating-point representation of the rational number.
   def __float__(self) :
      return float(self._numerator / self._denominator)
   
   # Compares this rational number to the rational number stored in
   # rhsFraction to determine their logical ordering.    
   def __eq__(self, rhsFraction) :
      if self._numerator == rhsFraction._numerator and \
         self._denominator == rhsFraction._denominator :
         return True  
      else :
         return False
   
   def __lt__(self, rhsFraction) :
      if (self._numerator * rhsFraction._denominator) < \
         (rhsFraction._numerator * self._denominator) :
         return True  
      else :
         return False
     
   def __le__(self, rhsFraction) :
      if (self._numerator * rhsFraction._denominator) > \
         (rhsFraction._numerator * self._denominator) :
         return True  
      else :
         return False   
      
   # Returns a new rational number that is the negative (-x) of this 
   # rational number.
   def __neg__(self) :
      negativeNum = Fraction(-1 * self._numerator, self._denominator)
      return negativeNum
   
   # Returns a new rational number that is the absolute version of this 
   # rational number.
   def __abs__(self) :
      return Fraction(abs(self._numerator), abs(self._denominator))
   
   #  Creates and returns a new rational number that is the result of adding
   # this rational number to the given rhsFraction.
   def __add__(self, rhsFraction) :
      newNum = ((self._numerator * rhsFraction._denominator) \
                + (rhsFraction._numerator * self._denominator))
      newDen = self._denominator * rhsFraction._denominator
      newFraction = Fraction(newNum, newDen)
      return newFraction 
   
   # The same as the add() operation but subtracts the two rational numbers.
   def __sub__(self, rhsFraction) :
      newNum = ((self._numerator * rhsFraction._denominator) \
                - (rhsFraction._numerator * self._denominator))
      newDen = self._denominator * rhsFraction._denominator
      newFraction = Fraction(newNum, newDen)
      return newFraction       
   
   # Creates and returns a new rational number that is the result of
   # multiplying this rational number to the given rhsFraction.
   def __mul__(self, rhsFraction) :
      newNum = self._numerator * rhsFraction._numerator
      newDen = self._denominator * rhsFraction._denominator
      newFraction = Fraction(newNum, newDen)
      return newFraction         

   # Creates and returns a new rational number that is the result of dividing
   # this rational number by the given rhsFraction. 
   # The rhsFraction can not be zero.
   def __truediv__(self, rhsFraction) :
      assert rhsFraction._denominator != 0 and rhsFraction._numerator != 0,\
             "The rhsFraction can not be zero."
      newNum = self._numerator * rhsFraction._denominator
      newDen = self._denominator * rhsFraction._numerator
      newFraction = Fraction(newNum, newDen)
      return newFraction      
  
   # Returns a string representation of the rational number in the format #/#.
   def __repr__(self) :
      return "%d/%d" %(self._numerator, self._denominator)
   
   