project_euler
=============
'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def total_sum(number):
    sum = 0
    num_range = range(number)
    for num in num_range:
        if num % 3 == 0 or num % 5 == 0:
            sum += num
    return sum    
            
print total_sum(1000)
