"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def primes(number_of_primes):

    if number_of_primes <= 0:
        raise ValueError
    else:
        list = []
        i = 2
        while len(list) < number_of_primes:
            if i == 2: 
               list.append(2)
               
            else:
               flag = True
               for number in range(2, i):
                   if i % number == 0:
                       flag = False     
            
               if flag == True:
                    list.append(i)

            i += 1
        
    return list
    #print(f'{list}') 
        
#print(primes(4))
