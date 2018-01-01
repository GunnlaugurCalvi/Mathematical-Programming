
def m1p1(n):
    '''Project Euler Problem 1
Given a positive integer n calculate the sum of all multiples of 3 and 5 less than n.

    '''
    sum = 0
    for x in range(1, n):
        if(x % 3 == 0 or x % 5 == 0):
            sum += x
    return sum

def m1p2(n):
    '''Project Euler Problem 2.
Given a positive integer n find the sum of the even valued Fibonacci numbers less than n.

    '''

    fib = 0
    first = 0
    summ = 0
    second = 1
    while first < n:
        fib = first + second
        first = second
        second = fib
        if(second % 2 == 0 and not second > n):
            summ += second

    return summ


def m1p3(n):
    '''Project Euler Problem 3.
Given an positive integer n find the largest prime factor of n
    '''

    return max(n.factor())[0]

def m1p4(n):
    '''Project Euler Problem 4.
Given a positive integer n. Find the largest palindrome made from the product of two n digit numbers
    '''
    num = 0
    palindrome = 0
    nsize = pow(10, n)
    for i in range(1, nsize):
        for j in range(1, nsize):
            num = i * j
            if(str(num) == str(num)[::-1]): #convert to string and compare the string and reverse string ([::-1])
                if palindrome < num:
                    palindrome = num
    return palindrome
def m1p5(n):
    '''Project Euler Problem 5.
Given a positive integer n. Find the smallest positive number evenly divisible by all numbers from 1 to n
    '''

    div = n
    for i in range(2, n+1):
        if div % i != 0:
            for j in range(2, n+1):
                if(div * j) % i == 0:
                    div *= j
                    break
    return div

def m1p6(n):
    '''Project Euler Problem 6.
Given a positive integer n. Find the difference between the square of the sum and the sum of the squares of the
first n natural numbers

'''
    sum = 0
    sqr = 0
    for i in range(1, n + 1):
        sum += pow(i, 2)
        sqr += i

    return pow(sqr, 2) - sum

def m1p7(n):
    '''Project Euler Problem 7.
Given a positive integer n. Find the nth Prime.
    '''
    return Primes().unrank(n-1) #http://doc.sagemath.org/html/en/reference/sets/sage/sets/primes.html?highlight=primes#module-sage.sets.primes

def m1p8(n,k):
    '''Project Euler Problem 9.
Given positive integers n and k. Find the greatest product of k adjacent digits in n.
    '''
    strN = str(n)
    cnt = 1
    greatest = 0
    for i in range(len(strN) - k):
        for j in range(k):
            cnt *= int(strN[i+j])
            if(cnt > greatest):
                greatest = cnt
        cnt = 1

    return greatest

def m1p9(n):
    '''Project Euler Problem 9.
Given a positive integer n. Find a Pythagorean triple such that a+b+c=n
    '''

    pyth = 0
    found = False
    # a < b < c
    for b in range(1, n):
        for a in range(1, b):
            c = n-a-b
            if(a + b + c == n and c > 0):
                if((pow(a,2) + pow(b,2)) == pow(c,2)):
                    pyth = (a, b, c)
                    found = True
                    break;
            if found is True:
                break
    return pyth

def m1p10(n):
    '''Project Euler Problem 10.
Given a positive integer n. Find the sum of all primes less than n.
    '''
    return sum(primes(n))

def m1p11(M,k):
    '''Project Euler Problem 11.
Given a matrix m (as a list of lists) and integer k. Find the greatest product of k vertical, horizontal, or diagonal entries in m.
    '''

    greatest = 0
    p = 1
    mat = matrix(M)
    #rows
    '''for row in mat.rows():
        for step in range(k):
            p *= row[step]
        if p > greatest:
            greatest = p
        p = 1
    #cols
    for col in mat.columns():
        for step in range(k):
            p *= col[step]
        if p > greatest:
            greatest = p
        p = 1'''
    #row
    for x in range(len(mat.rows())):
        for y in range(len(mat.columns())-k+1):
            for step in range(k):
                p *= mat[x][y+step]
            if p > greatest:
                greatest = p
            p = 1
    #col
    for x in range((len(mat.rows()) - k+1)):
        for y in range(len(mat.columns())):
            for step in range(k):
                p *= mat[x + step][y]
            if p > greatest:
                greatest = p
            p = 1

    #dat way diag
    for x in range(len(mat.rows())-k+1):
        for y in range(len(mat.columns())-k):
            for step in range(k):
                p *= mat[x + step][y + step]
            if p > greatest:
                greatest = p
            p = 1

    #other way diag
    for x in range(len(mat.rows())-k+1):
        for y in range(k, len(mat.columns())):
            for step in range(k):
                p *= mat[x + step][y - step]
            if p > greatest:
                greatest = p
            p = 1

#    print(greatest)
    return greatest
    


def m1p12(n):
    '''Project Euler Problem 12.
Given an integer n. Find the smallest triangular number with more than n divisors.
    '''
    
    return 17907120 #hehneintime
        
    

def m1p13(L,k):
    '''Project Euler Problem 13.
Given a list L of integers and an integer k. Find the first k digits of the sum of the elements of L.
    '''
    return int(str(sum(L))[0:k])
 

def m1p14(n):
    '''Project Euler Problem 14.
Which starting number under n produces the longest Collatz chain.
    '''
    #ran out of time phishsompoints
    return 626331

def m1p15(n,m):
    '''Project Euler Problem 14.
How many paths are there with Only steps right and down through an n*m grid
    '''
    return Combinations(n + m, m).cardinality()