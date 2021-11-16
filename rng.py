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
     
    #check in which interval the random number falls

    for j in range(n_interval):
       if (s > float(j)*interval_length) and (s <= float(j+1)*interval_length):
           counter[j] = counter[j] + 1
           break

# print the number of RNs in each interval
#for i in range(n):
    #print("For interval ",round(i*interval_length,1)," to ",\
    #round((i+1)*interval_length,1)," = ",counter[i])


import matplotlib.pyplot as plt 

# x axis values 
x = [interval_length*i for i in range(n_interval)]
# corresponding y axis values 
#print(x)
#print(counter)

# plotting the points  
plt.bar(x, counter,width = 0.05) 
#plt.hist(x,counter)    
# naming the x axis 
plt.xlabel('Intervals') 
# naming the y axis 
plt.ylim(500,1500)
plt.ylabel('RN counts') 
    
# giving a title to my graph 
plt.title('RN uniformity') 
    
# function to show the plot 

plt.show() 
#exit()

radius = 1
trials = 1000
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
    #print(format(pi,".5f"))
    pia[i] = pi
    #print(pia[i])

x = [i for i in range(trials)]
# plotting the points  
plt.plot(x, pia) 
    
# naming the x axis 
plt.xlabel('TRIALS (with ' + str(incriment) + ' random number for each trial)') 
# naming the y axis 
#plt.ylim(500,1500)
plt.ylabel('Pi value') 
    
# giving a title to my graph 
plt.title('Pi estimation') 
    
# function to show the plot 
plt.show() 



