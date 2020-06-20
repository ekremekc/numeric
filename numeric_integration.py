import numpy as np
import matplotlib.pyplot as plt


x_start  = 0
x_finish = 5
dx=0.0001

x_array = np.arange(x_start, x_finish+dx , dx)

def y(x):
    return x**2
def y_int(x):
    return (x**3)/3

analytic_result = y_int(x_finish) - y_int(x_start)

############## RECTANGULAR INTEGRAL METHOD
total = 0

for x in x_array:
    
    if x ==x_finish:
        break
    
    area = dx*y(x)
    
    total+=area

############## TRAPEZOIDAL INTEGRAL METHOD
total_t = 0

for x in x_array:
    
    if x == x_finish:
        break
    
    area_t = dx*(y(x)+y(x+dx))/2
    
    total_t+=area_t

############## SIMPSON RULE
    
n = 6

coef_matrix = np.array([1])

for k in range(0,n):
    if (k%2==0):
        coef_matrix=np.append(coef_matrix,4)
    elif(k%2==1) and (k!=n-1):
        coef_matrix=np.append(coef_matrix,2)
    if k==n-1:
        coef_matrix=np.append(coef_matrix,1)

x_simpson = np.linspace(x_start, x_finish,n+1)
y_simpson = y(x_simpson)

total_s = sum(((x_finish-x_start)/6)/3*(coef_matrix*y_simpson))

############################

print("Analytical Result:\t\t\t ",analytic_result)       
print("Rectangular Integral Method Result:\t ",total)
print("Trapezoidal Integral Method Result:\t ",total_t)
print("Simpson Integral Method Result:\t\t ",total_t)







