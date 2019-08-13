#plots scatter of some numbers from a floating point representation


import numpy as np
import matplotlib.pyplot as plt

largest_num = 0b111
max_exponent = 3
min_exponent = -3 

mantissa_array = [largest_num-i+1 for i in range(2**int.bit_length(largest_num))]
mantissa_array_neg = [-i for i in mantissa_array] 
mantissa_array.reverse() 
mantissa_array =mantissa_array_neg + mantissa_array
print(mantissa_array)

exponent_array = [i for i in range(min_exponent,max_exponent+1, 1)]
print(exponent_array)

convert = lambda mantissa, exponent: mantissa*(2**exponent)

numbers = [convert(i,j) for i in mantissa_array for j in exponent_array]
numbers.sort()
print(numbers)

plt.plot(numbers, np.zeros_like(numbers), 'bo')
plt.show()
