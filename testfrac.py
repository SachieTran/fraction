# testfrac.py
#
# Created by: Sachie Tran
# Date: 3/1/2016
# 
# This program tests the Fraction ADT in fraction.py

from fraction import Fraction 

# Create some fractions
myFraction1 = Fraction(1, -2)
myFraction2 = Fraction(-6, 3)
myFraction3 = Fraction(0, 7)
myFraction4 = Fraction(-5, -2)

# Print the results
print()
print("The fraction 1 is: ", myFraction1)
print("The fraction 2 is: ", myFraction2)
print("The fraction 3 is: ", myFraction3)
print("The fraction 4 is: ", myFraction4)
print()
print("The numerator of fraction 1: ", myFraction1.getNum())
print("The denominator of fraction 1: ", myFraction1.getDen())
print("Is the fraction 2 equal zero? -> ", myFraction2.isZero())
print("Is the fraction 1 negative? -> ", myFraction1.isNegative())
print("The reciprocal of fraction 1: ", myFraction1.reciprocal())
print("The float value of fraction 1: ", float(myFraction1))

if myFraction2 == myFraction3 :
   print("The fraction 2 is equal fraction 3.")
elif myFraction2 < myFraction3 :
   print("The fraction 2 is smaller than fraction 3.")
else : 
   print("The fraction 2 is larger than fraction 3.")
      
print("The negative value of fraction 1: ", -(myFraction1))
print("The absolute value of fraction 1: ", abs(myFraction1))
print("The result of adding fraction 4 to fraction 3: ",\
      (myFraction3 + myFraction4))
print("The result of subtracting fraction 1 by fraction 3: ",\
      (myFraction1 - myFraction3))
print("The result of multiplying fraction 1 with fraction 2: ",\
      (myFraction1 * myFraction2))
print("The result of dividing fraction 1 by fraction 4: ",\
      (myFraction1 / myFraction4))


