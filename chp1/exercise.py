"""
Chapter 0ne  Exercises of the Data Structure and Algorithms in Python by Michael T Goodrich et al
An exercise to improve and strengthen your programming skills in Python 
"""

# R-1.1
"""
Write a short Python Function, is_multiple(n,m) that
takes two integer values and returns True if n is a 
multiple of m , that is 'n = mi' for some integer 'i' 
and False otherwise
"""


def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

# R-1.2
"""
Write a short Python function, is_even(k),
that takes an integer value and returns True if K is even,
and False otherwise.However, your function 
cannot use the multiplication and modulo or division operator
"""

#def is_even(k):
    #if k

# R-1.3
"""
Write a short Python , minmax(data), that takes a sequence of
one or more numbers and returns the smallest and largest numbers in the 
form of a tuple of length two. Do not use the built-in functions min or max
in implementing the solutions
"""

def min_max(data):
   
    maxi = data[0]
    mini = data[0]
    
    for ele in data:
        if ele > maxi :
            maxi = ele
        
        elif ele < mini:
            mini = ele

    return maxi, mini

#R-1.4
"""
Write a short Python Function that takes a positive integer n and retuens 
the sum of squares of all the positive integers smallthan n
"""
def sum_of_squares(n):
    n -= 1
    sum_sq = 0
    while n > 0:
        sum_sq += n**2
        n -= 1
    return sum_sq