
def solution(n, b):
    
    k = len(n)
    
    # Store results of Algorithm so we can check for cycles
    algorithm_results = []
    
    while True:
        
        # Convert n string into a list of digits
        n = list(n)
        
        x = sorted(n, reverse=True)
        y = sorted(n)
        
        # Convert bases
        x = base10(x, b, k)
        y = base10(y, b, k)
        
        z = x-y
        
        # convert back to base b 
        z = baseb(z, b, k)  
        
        # We now have a list of digits that we need to check the length of
        if len(z) < k:
            _ = k - len(z)
            for i in range(_):
                z.insert(0, 0)
        
        # join back into a string        
        z = str(''.join(str(_) for _ in z))
        
        # check for cycles
        if z in algorithm_results:
            # if cycle, the length is the cur len of results list - index 
            # of the number last time it arose
            X = algorithm_results.index(z)
            result = (len(algorithm_results) - X)
            
            return result
         
        else:
            algorithm_results.append(z)
        n = z

def baseb(n, b, k):
    
    # converting from base 10 back to base b
    
    powers = []
    for i in range(k):
        powers.append(i)
    powers.sort(reverse=True)
    
    columns = []
    for i in range(k):
        columns.append(b**powers[i])
    
    _ = n
    result = []
    for i in columns:
        try:
            j = _/i
        except ZeroDivisionError:
            j = 0
        result.append(int(j))
        try:
            _ = _%i
        except ZeroDivisionError:
            _ = 0 
            
    return result       



def base10(n, b, k):

    # converting from base b to base10
    powers = []
    for i in range(k):
        powers.append(i)
    powers.sort(reverse=True)
    
    columns = []
    for i in range(k):
        columns.append(b**powers[i])
    
    n = list(n)
    
    result = 0
    
    for i in range(k):
        result = result + ((int(n[i]))*(int(columns[i])))
    
    return result
    
        
        
        
        
#####
NOTES
#####

# The algorithm takes a number in a specific base.


# ALGORITHM
# 1) b = base (between 2 and 10)
# 2) k = len(n)
# 3) x = elements of n in DESCENDING ORDER
# 4) y = elements of n in ASCENDING ORDER 
# 5) z = x - z (if len z<k add leading 0s)
# -> subtracting numbers in none base 10 is different to subtracting base 10 numbers
# ---> to solve this we will create a function to turn the numbers into base 10
# ---> subtract the base 10 numbers 
# ---> convert the result back to original base (b)
# ---> add leading 0s to make the length back to normal

# DETECTING CYCLE
# -> the algorithm will eventually crash and keep returning the same number. 
# -> The goal of this code is to find the 'length of the cycle'
# --> n = 123 ... n = 452 ... n = 143  .... n = 123 for example, the length of this cycle would be 3 (?)
#    \______/     \______/    \______/     \______/
#        1           2            3            1  

# 1) each 'n' is added to a list of 'ids'
# 2) check whether each 'n' has previously arisen in the 'ids' list 
# 3) if yes, the length of the cycle is the difference between the two elements

# ie [012][415][138][492][830][467][900][895][467][..]
# el ->0    1    2    3    4    5    6    7    8 
# check                         *              *
# 8 - 5 = 3
# cycle length = 3