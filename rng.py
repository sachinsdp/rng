# PG lab linear congruential genertor
#######################################################################
# Problem 1 a)

# choose variable according to the below conditions.
# 0 < a < m  # 0 ≤ c < m  # 0 ≤ X0 < c 
x = 7 
c = 13 
a = 3 
m = 20 
n = 10 
y = 0.0 

print("Problem 1.A \n Random numbers generated are \n")
for i in range(n):
  x = (a*x + c) % m  # LCG equation
  y = x/m
  print(y)           # Print Random numbers

########################################################################
# Problem 1 b)

# m = 2^32	a = 1664525	c = 1013904223 (Numerical recipes book)
print("\n Problem 1.B \n Random numbers generated are \n")
x = 1  
c = 1013904223 
a = 1664525 
m = 2**32 
n = 10 
y = 0.0

for i in range(n):
  x = (a*x + c) % m
  y = x/m
  print(y)

########################################################################
# Problem 2

print("\n problem 2. \n Test for uniformity of Pyhton inbuilt random number \
generator \n")

# uniformity
n_interval = 10
counter = [0] * n_interval
interval_length = (1/n_interval)
n_rn = 10000

print("Number of intervals taken is = ",n_interval)
print("length of interval is = ",interval_length,"\n \n")

import random as rn

rn.seed(10)

# generate Random numbers
for i in range(n_rn):

    s = rn.random()
     
    #check in which interval the random number falls into

    for j in range(n_interval):
       if (s > float(j)*interval_length) and (s <= float(j+1)*interval_length):
           counter[j] = counter[j] + 1
           break

import matplotlib.pyplot as plt 

# x axis values 
x = [interval_length*i for i in range(n_interval)]

# plotting the points  
plt.bar(x, counter,width = 0.05) 

plt.xlabel('Intervals') 

plt.ylim(500,1500)
plt.ylabel('RN counts') 

plt.title('RN uniformity') 

plt.show() 


# estimation of Pi by monte carlo

radius = 1
trials = 100
incriment = 1000
inside = 0

pia = [0] * trials

for i in range(trials):

    for j in range(incriment):
        x = 2 * rn.random() - 1
        y = 2 * rn.random() - 1
        z = x*x + y*y
        if(z <= 1.0):
            inside = inside + 1
    pi  = 4 * (inside/(incriment*(i+1)))

    pia[i] = pi

x = [i for i in range(trials)]
 
plt.plot(x, pia) 

plt.xlabel('TRIALS (with ' + str(incriment) + ' random number for each trial)') 

plt.ylabel('Pi value') 
    
plt.title('Pi estimation') 
    
plt.show()