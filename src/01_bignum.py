# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

#---------------------------------------------------------------------
'''
  How is it done in JavaScript:
  base ** exponent;  
  Math.pow(base, exponent);
'''

# In Python there are three ways to exponentiate values:  

# 1. returns an integer
doubleAsterisk = 2 ** 65536; 

# 2. returns an integer 
builtInPower = pow(2, 65536); 

# 3. returns a double, caps input value at about 1000
import math; 
mathPower = math.pow(2, 6);

print(doubleAsterisk); 
