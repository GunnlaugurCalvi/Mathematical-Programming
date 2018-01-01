def mCp1(x,y):
    '''Return the Euclidean distance between x and y
    '''
    #float(round(pow(pow(q[0] - p[0],2) + pow(q[1] - p[1],2) , (1/2.0)),2))
    bla = 0
    for i in range (len(x)):
        bla += pow(x[i] - y[i],2)

    return float(round(sqrt(bla),2))

def mCp2(x, y):
    '''Return the Manhattan distance between x and y
    '''
    #return abs(q[0] - p[0]) + abs(q[1] - p[1])
    bla = 0
    for i in range(len(x)):
        bla += abs(x[i] - y[i])

    return float(round(bla,2))
def mCp3(x, y):
    '''Retun the Hamming distance between x and y
    '''
    bla = 0
    for i in range(len(x)):
        if bool(x[i]) != bool(y[i]):    #XOR python operator ^
            bla += 1
    return bla

def mCp4(x, y):
    '''Return the Levenshtein distance between x and y
    '''
    mat = matrix(ZZ, len(x)+1,len(y)+1, [list(range(len(x)+1)) if i == 0 else [i]+[0]*(len(x)) for i in range(len(y)+1)]) #another way of making matrix of a double list

#     mat = matrix(len(x)+1, len(y)+1)

    if len(x) == 0 or len(y) == 0:
        return len(max(x,y))

#     for i in range(0,len(x)+1):
#         mat[i,0] = i
#     for j in range(0, len(y)+1):
#         mat[0,j] = j

    for i in range(1, len(y)+1):
        for j in range(1, len(x)+1):
            if x[i-1] == y[j-1]:
                c = 0
            else:
                c = 1
            mat[i,j] = min(mat[i-1,j] + 1,
                          mat[i,j-1] + 1,
                          mat[i-1,j-1] + c)
    return mat[len(y),len(x)]


def mCp5(x, y):
    '''Return the rank distance of the matrices constructed from x and y
    '''
    return rank(matrix(RR, sqrt(len(x)), sqrt(len(x)), x) - matrix(RR, sqrt(len(y)), sqrt(len(y)), y)) #beautiful

def mCp6(L):
    '''Check whether L satisfies the axiom of neighborliness w.r.t the Hamming distance
    '''
    bla = []
    for i in range(len(L)):
        minDist = len(L[i][0])
        label = L[i][1]
        for j in range(len(L)):
            if i != j:
                dist = mCp3(L[i][0],L[j][0])
                if dist < minDist:
                    minDist = dist
                    #label = L[j][1]
                    bla = j
        if L[i][1] != L[bla][1]:
            return False
    return True
def mCp7(L, J):
    '''Use the labeled points in L to label the points in J using the nearest neighbor in the Hamming distance
    '''
    bla = []
    tmp = []
    for i in range(len(J)):
        minDist = len(J[i])
        label = 10
        for j in range(len(L)):
            dist = mCp3(J[i] , L[j][0])
            if dist <= minDist:
                minDist = dist

        bla.append((J[i],label))
    return bla

# from statistics import mode
def mCp8(L, J, k):
    '''Use the labeled points in L to label the points in J using the k nearest neighbors in the Hamming distance
    '''

    bla = []
    label = 100
    if not J:
        return []

    for i in range(len(J)):
        minDist = len(J[i])
        lis = []
        for j in range(len(L)):
            lis.append([mCp3(J[i] , L[j][0]), L[j][1]])
        lis = sorted(lis, key=lambda x: (x[0],x[1]))
        lis = lis[:k]
        for z in range(len(lis)):
            lis[z] = lis[z][1]

        if len(lis) == len(set(lis)):
            label = min(lis)
        else:
            label = max(set(lis), key=lis.count)
        bla.append((J[i],label))
    return bla 

