
def fib_seq(number):
    num_list = [number, number + number]
    sum = 0
    
    while num_list[-1] < 4000000:
        num_list.append(num_list[-1] + num_list[-2]) 
    
    for num in num_list:
        if num % 2 == 0:
            sum += num
            
            
    return sum      

print fib_seq(1)
    
