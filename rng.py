# PG lab linear congruential genertor
#######################################################################
# Problem 1 a)

# choose variable according to the below conditions.
# 0 < a < m  # 0 ≤ c < m  # 0 ≤ X0 < c 
x = 7 ; c = 13 ; a = 3 ; m = 20 ; n = 10 ; y = 0.0
print("Problem 1.A \n Random numbers generated are \n")
for i in range(n):
  x = (a*x + c) % m  # LCG equation
  y = x/m
  print(y)           # Print Random numbers

########################################################################
# Problem 1 b)

# m = 2^32	a = 1664525	c = 1013904223 (Numerical recipes book)
print("\n Problem 1.B \n Random numbers generated are \n")
x = 1 ; c = 1013904223 ; a = 1664525 ; m = 2**32 ; n = 100 ; y = 0.0

for i in range(n):
  x = (a*x + c) % m
  y = x/m
  print(y)

########################################################################
# Problem 2

print("\n problem 2. \n Test for uniformity of Pyhton inbuilt random number \
generator \n")

# uniformity
n = 10
counter = [0] * n
interval_length = (1/n)


print("Number of intervals taken is = ",n)
print("length of interval is = ",interval_length,"\n \n")

import random as rn

rn.seed(10)

# generate Random numbers
for i in range(10000):

    s = rn.random()
     
    #check in which interval the random number falls

    for j in range(n):
       if (s > float(j)*interval_length) and (s <= float(j+1)*interval_length):
           counter[j] = counter[j] + 1
           break

# print the number of RNs in each interval
for i in range(n):
    print("For interval ",round(i*interval_length,1)," to ",\
    round((i+1)*interval_length,1)," = ",counter[i])