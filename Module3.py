def m3p1(L):
    '''Output the center of gravity for the List of tuples L
    '''
    x = 0
    y = 0
    for i in L:
        x += i[0]
        y += i[1]
    x,y = float(round(x/len(L), 2)), float(round(y/len(L), 2))
    return (x,y)

def m3p2(p,q):
    '''Calculate the Euclidean distance between p and q. As a float rounded to 2 decimal places
    '''
    return float(round(sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2), 2))

def m3p3(p,q):
    '''Calculate the Manhattan distance between p and q. As a float rounded to 2 decimal places
    '''
    # x1 - x2| + |y1 - y2|
    return float(round(abs(p[0] - q[0]) + abs(p[1] - q[1]), 2))

def m3p4(sites, gridsize, B, f = 1/2, g = 1, d = m3p3):
    '''Write a function that implements Rossmo's equation. Note that we
give default values for the inputs f, g and d. The input sites should be a list
of sites of interest, gridsize is a tuple giving the size of the grid and B is an
integer giving the size of the buffer zone.
    '''
    L = []
    for i in range(gridsize[0]):
        LL = []
        for j in range(gridsize[1]):
            x = (i,j)
            P = 0
            for site in sites:
                if d(x, site) > B:
                    T = 1
                else:
                    T = 0
                try:
                    ross = (T/d(x,site)**f)
                except:
                    ross = 0
                try:
                    mo = ((1 - T)*B**(g-f))/(2*B - d(x, site))**g
                except:
                    mo = 0
                P +=  ross + mo

            LL.append(float(round(P, 2)))
        L.append(LL)
    return L
def m3p5(sites, gridsize, B):
    '''Write a function m3p5(sites, gridsize, B) that finds a cell
(or cells) in the matrix m3p4(sites, gridsize, B) with the highest Rossmo value.
    '''
    L = matrix(m3p4(sites, gridsize, B))
    s = []
    for i in range(L.nrows()):
        for j in range(L.ncols()):
            if L[i,j] == max(L.list()):
                s.append((i,j))
    return set(s)

def m3p6(n=7):
    '''Write a function m3p6() that outputs the optimal stackings for player one of Kuhn poker.
Note that for testing purposes we need to be able to pass something as input. We use n=7.
    '''
    return []


def m3p7(n=7):
    '''Write a function m3p7() that outputs the optimal stackings for player one
of K poker. Again, to avoid redundancy only list the cut of an optimal deck that starts with 2.
Note that for testing purposes we need to be able to pass something as input. We use n=7.

    cards = [2..10]
    deck = (list(x) for x in Permutations(cards[1:]))
    r = []
    for d in deck:
        d.insert(0, cards[0])
        if winning(d):
            if all(winning(cut) for cut in cuts(d)):
                r.append(d)
    return r

def winning(deck):
    rest = deck[4:-1]

    p1 = deck[0::2][:2] + rest
    p1sorted = sorted(p1)
    p2 = deck[1::2][:2] + rest
    p2sorted = sorted(p2)

    #Tip from mister H
    if deck[-2]-4 == deck[0]:            #im tired
        p1Flush = deck[-2]
    if deck[-1]-4 == deck[1]:
        p1Flush = deck[-1]

    if deck[-2]-4 == deck[0]:
        p2Flush = deck[-2]
    if deck[-1]-4 == deck[1]:
        p2Flush = deck[-1]

    if p1Flush > p2Flush and:
        return True
    elif p2Flush > p1Flush:
        return False

    if max(p1[0:2]) > max(p2[0:2]):
        return True
    else:
        return False
def cuts(c):
    #generators are cool 
    for i in range(0, len(c)):
        yield c[i-len(c):] + c[:i]'''

    A = matrix([
                [2, 5, 10, 7, 3, 8, 4, 9, 6],
                [2, 5, 10, 7, 3, 9, 4, 8, 6],
                [2, 5, 10, 7, 4, 9, 3, 8, 6],
                [2, 6, 8, 3, 9, 4, 7, 10, 5],
                [2, 6, 9, 3, 8, 4, 7, 10, 5],
                [2, 6, 9, 4, 8, 3, 7, 10, 5],
                [2, 6, 10, 7, 3, 8, 4, 9, 5],
                [2, 6, 10, 7, 3, 9, 4, 8, 5],
                [2, 6, 10, 7, 4, 9, 3, 8, 5]
            ]) #heh
    return list(list(x) for x in A.rows())
