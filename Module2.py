P = 1
NP = 0
def m2p1(n):
    '''Given a non-negative integer n calculate n-th Tribonacci number, using recursion.
    '''
    if n <= 1:
        return 0
    if n == 2:
        return 1
    return m2p1(n - 1) + m2p1(n - 2) + m2p1(n - 3)



memo = {0:0, 1:0, 2:1}
def m2p2(n):
    '''Given a non-negative integer n calculate n-th Tribonacci number, using recursion and memoization.
    '''
    lit = 0
    if n in memo:
        return memo[n]
    else:
        lit = m2p2(n - 1) + m2p2(n - 2) + m2p2(n - 3)
        memo[n] = lit
        return lit

def m2p3(n):
    '''Given a non-negative integer n calculate n-th Tribonacci number using memoization with a list, and without using recursion
        '''
    # Initializing a list to contain the values
    T = [0,0,1] + [0]*(n-2)
    for i in range(3,n+1):
        T[i] = T[i - 1] + T[i - 2] + T[i - 3]
    return T[n]


def m2p4(n):
    '''Given a non-negative integer n calculate n-th Tribonacci number, without using recursion and only storing three values.
    '''
    nth = 0
    if n <= 1:
        return 0
    t3, t2, t1 = 1,0,0 #t3 = sum of all t's,t2 = last value of t3,t1 = last value of t2
    for i in range(3,n+1):
        t1,t2,t3 = t2,t3,t1+t2+t3
    return t3

def m2p5(n,L):
    '''Project Euler Problem 31.
The input n is a positive integer and the input L is a list of coin values.
The returned value is the number of ways n can be split using the coin values in the list L.
    '''
    total = [1] + [0] * n
    for c in L:
        for i in range(c, n+1):
            total[i] += total[i - c]


    return total[n]

def m2p6(k):
    '''Project Euler Problem 76.
The input k should be a positive integer. The returned value is the number of
different ways k can be written as a sum of at least two positive integers.
    '''

    return (len(Partitions(k))-1)

def m2p7(k):
    '''Project Euler Problem 77.
The input k should be a positive integer. The returned value is the smallest positive
integer n such that the number of ways to write n as a sum of primes exceeds k
    '''
    primetime = list(primes(1, 1337))
    #p = Partitions(k)
    cnt = 0
    while P is not NP:
        total =  [1] + [0] * cnt
        for i in primetime:
            for j in xrange(i, cnt+1):

                total[j] = total[j] + total[j-i]
                #print total[j]
        if total[cnt] > k:
            break

        cnt += 1

    if k in primetime:
        cnt += 1

#     print cnt
    return cnt
def m2p8(k):
    '''Project Euler Problem 78.
The input k should be a positive integer. The returned value is the smallest positive
integer n such that number of ways n coins can be separated into piles is divisible by k.
    '''
    return Partitions(k).cardinality()


def m2p9(M):
    '''Project Euler Problem 81.
The input M should be an n x n matrix containing integers, given as a list of lists.
The output is the minimal path sum, as defined on Project Euler.
    '''
    
    return -1

