NO_OF_CHARS = 1000
def substring1(str, n): 
    count = [0] * NO_OF_CHARS 
    for i in range(n): 
        count[ord(str[i])] += 1
    max_distinct = 0
    for i in range(NO_OF_CHARS): 
        if (count[i] != 0): 
            max_distinct += 1    
    return max_distinct 
def substring2(str): 
    n = len(str)     
    max_distinct = substring1(str, n) 
    minl = n    
    for i in range(n): 
        for j in range(n): 
            subs = str[i:j] 
            subs_lenght = len(subs) 
            sub_distinct_char = substring1(subs,  
                                                  subs_lenght) 
            if (subs_lenght < minl and 
                max_distinct == sub_distinct_char): 
                minl = subs_lenght 
    return minl 
if __name__ == "__main__": 
    str = input()
    l = substring2(str) 
    print( "The length of the smallest substring is:", l) 
