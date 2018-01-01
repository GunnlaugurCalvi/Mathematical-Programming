def m4p1(p):
    '''Output the number of inversions
    '''
    count = 0
    for i in range(len(p)):
        for j in range(len(p)) :
            if p[i] > p[j] and i < j:
                count += 1

    return count
def m4p2(p):
    '''Return the number of descents
    '''
    count = 0
    for i in range(len(p)):
        for j in range(len(p)) :
            if p[i] > p[j] and i < j and p[i+1] == p[j]:
                count += 1
    return count
def m4p3(n):
    '''Return the number of permutations that have the same amount of inversions and descents
    '''
    a = 0
    b = 1
    c = 0
    res = 0

    if n == 0:
        return 1

    while c < n:
            res = a + b
            a = b
            b = res
            c += 1

    return res


def m4p4(p, cl):
    '''Input True if the permutation p contains the classical pattern cl
    '''

    L = Combinations(p, len(cl))
    lis = m4p7(p)
    for i in L:
        if m4p7(i) == cl:
            return True
    return False

def m4p5(p):
    '''Return the permutation after one pass with bubble-sort
    '''

    '''end = max(p)
    i = 0
    tmp = 0
    while end != p[-1]:
        if p[i] > p[i+1]:
            tmp = p[i]
            p[i] = p[i+1]
            p[i+1] = tmp
            i += 1
        else:
            i += 1
    return p'''
    tmp = 0
    for i in xrange(len(p)-1):
        if p[i] > p[i+1]:
            tmp = p[i]
            p[i] = p[i+1]
            p[i+1] = tmp
    return p

def m4p6(n=7):
    '''Return the correct classical patterns
    '''

    res = [1,2,3]
    lis = list(Permutations(res))
    result = []
    for i in lis:
        bla = m4p5(list(i))
        if bla != res:
            result.append(i)

    return result            #[[2,1,3],[3,2,1]]

def m4p4_list(p, M): return any(m4p4(p, cl) for cl in M)

def av(M, n): return [p for p in Permutations(n) if not m4p4_list(list(p),M)]

def bubble_sortable(n): return [p for p in Permutations(n) if m4p5(list(p)) == range(1,len(p)+1)]

def m4p7(p):
    '''Return the standardization of p
    '''
    sP = sorted(p)
    L = []
    for i in p:
        for j in range(len(sP)):
            if i == sP[j]:
                L.append(sP.index(i)+1)
    return L

def m4p8(L):
    '''Return the classical patterns the permutaions in L avoid, if possible. Otherwise False
    '''
    return []

