from random import random
import decimal 
import numpy as np
import math
from random import randint
from matplotlib import pyplot as plt
stored_values = []
# We assume 365 days in a year
# Given probability p,
# For each value of number of students k, we want to be checking if log(365!) - log(365-k!) - klog(365) <= 1 - p : If yes, the probability of two students having the same birthday in a class of k students is more than p.
def myfunc(students) :
    val = 0
    k = students
    # storing value log(365!) - log((365-k)!) - klog(365)
    for i in range(366-k,366):
        val += math.log10(i)
    val1 = math.log10(365)
    val1 *= k
    val -= val1
    return val
def myfunc1():
    for i in range(0,366):
        number_of_ppl = i
        probability = myfunc(number_of_ppl)
        stored_values.append(probability)
    
 
def myfunc2(probability):
    if(probability == 0):
      return 0
    if(probability == 1):
      return 365
    num_of_ppl = 0
    probability = 1 - probability
    probability = math.log10(probability)
    for i in range(2,366):
        num_of_ppl = i
        if(stored_values[i] <= probability):
            break
        #finding the minimum people we need to 
    return num_of_ppl
def myfunc3():
     num_ppl = [0,1]
     probabilities = [0,0]
     for i in range(2,366):
        num_ppl.append(i)
        val = myfunc(i)
        val = 10 ** val
        val = 1- val
        probabilities.append(val)
    #print(val)
    # plotting the values
     plt.plot(num_ppl,probabilities, marker='o', linestyle='-')
     plt.xlabel('Number of people')
     plt.ylabel('Probabilities')
     plt.title('Plot between number of people and probabilities')
     plt.ylim(0,1)
     plt.xlim(0,100)
     plt.savefig('plots.png')
    
def main():
    myfunc1()
    myfunc3()
    probability = 0

    while (probability != -1):
       print("Enter -1 to exit.")
       probability = (decimal.Decimal)(input("Enter Probability: "))
       if(probability == -1):
          break
       if(probability>1 or probability<0 ):
           print("INVALID_INPUT")
           break
       min_num_ppl = myfunc2(probability)
       print("Minimum number of people needed : ",min_num_ppl)
    
if __name__ == '__main__':
    main()