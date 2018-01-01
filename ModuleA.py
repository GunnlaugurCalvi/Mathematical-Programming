def mAp1(A,c):
    '''Output the state of the cell after one iteration
    '''
    newA = matrix(A)
    L = []
    cnt = 0
    ret = 0
    try:
        L.append(newA[c[0]-1][c[1]])
    except:
        L.append(0)
    try:
        L.append(newA[c[0]-1][c[1]+1])
    except:
        L.append(0)
    try:
        L.append(newA[c[0]][c[1]+1])
    except:
        L.append(0)
    try:
        L.append(newA[c[0]+1][c[1]+1])
    except:
        L.append(0)
    try:
        L.append(newA[c[0]+1][c[1]])
    except:
        L.append(0)
    try:
        L.append(newA[c[0]+1][c[1]-1])
    except:
        L.append(0)
    try:
        L.append(newA[c[0]][c[1]-1])
    except:
        L.append(0)
    try:
        L.append(newA[c[0]-1][c[1]-1])
    except:
        L.append(0)

    for i in range(len(L)):
        if L[i] == 1:
            cnt += 1

    if newA[c] == 1:
        if cnt <= 1:
            ret = 0
        if cnt <= 4:
            ret = 0
        if cnt == 3 or cnt == 2:
            ret = 1
    if newA[c] == 0:
        if cnt == 3:
            ret = 1
        else:
            ret = 0
    return ret

def mAp2(A):
    '''Output the state of the matrix after one iteration
    '''
    newA = matrix(A)
    retA = matrix(A)
    for i in range(newA.nrows()):
        for j in range(newA.ncols()):
            cnt = 0
            L = []
            try:
                if i-1 >= 0 and j >= 0:
                    L.append(newA[i-1,j])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i-1 >= 0 and j+1 >= 0:
                    L.append(newA[i-1,j+1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i >= 0 and j+1 >= 0:
                    L.append(newA[i,j+1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i+1 >= 0 and j+1 >= 0:
                    L.append(newA[i+1,j+1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i+1 >= 0 and j >= 0:
                    L.append(newA[i+1,j])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i+1 >= 0 and j-1 >= 0:
                    L.append(newA[i+1,j-1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i >= 0 and j-1 >= 0:
                    L.append(newA[i,j-1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i-1 >= 0 and j-1 >= 0:
                    L.append(newA[i-1,j-1])
                else:
                    L.append(0)
            except:
                L.append(0)
            for x in range(len(L)):
                if L[x] == 1:
                    cnt += 1

                if newA[i,j] == 1:
                    if cnt <= 1:
                        retA[i,j] = 0
                    if cnt <= 4:
                        retA[i,j] = 0
                    if cnt == 3 or cnt == 2:
                        retA[i,j] = 1
                elif newA[i,j] == 0:
                    if cnt == 3:
                        retA[i,j] = 1
                    else:
                        retA[i,j] = 0

    return list(list(row) for row in retA.rows())

def mAp3(A,k):
    '''Output the state of the matrix after k iterations
    '''
    for i in range(0, k):
        repeatedMAp2(A)
    return A

def repeatedMAp2(A):                #To avoid conflict in problem 3 and 6
    newA = matrix(A)
    for i in range(newA.nrows()):
        for j in range(newA.ncols()):
            cnt = 0
            L = []
            try:
                if i-1 >= 0 and j >= 0:
                    L.append(newA[i-1,j])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i-1 >= 0 and j+1 >= 0:
                    L.append(newA[i-1,j+1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i >= 0 and j+1 >= 0:
                    L.append(newA[i,j+1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i+1 >= 0 and j+1 >= 0:
                    L.append(newA[i+1,j+1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i+1 >= 0 and j >= 0:
                    L.append(newA[i+1,j])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i+1 >= 0 and j-1 >= 0:
                    L.append(newA[i+1,j-1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i >= 0 and j-1 >= 0:
                    L.append(newA[i,j-1])
                else:
                    L.append(0)
            except:
                L.append(0)
            try:
                if i-1 >= 0 and j-1 >= 0:
                    L.append(newA[i-1,j-1])
                else:
                    L.append(0)
            except:
                L.append(0)
            for x in range(len(L)):
                if L[x] == 1:
                    cnt += 1

                if newA[i,j] == 1:
                    if cnt <= 1:
                        A[i][j] = 0
                    if cnt <= 4:
                        A[i][j] = 0
                    if cnt == 3 or cnt == 2:
                        A[i][j] = 1
                elif newA[i,j] == 0:
                    if cnt == 3:
                        A[i][j] = 1
                    else:
                        A[i][j] = 0

    return A

def mAp4(A,k):
    '''Output the state of the matrix after k iterations,
doing as little work as possible
    '''
    for i in xrange(0,k):
        mat = repeatedMAp2(A)
        isDead = 0
        for x in xrange(len(mat)-1):
            for y in xrange(len(mat)-1):
                isDead += mat[x][y]
        if isDead == 0:
            break
    return A

def mAp5(n=7):
    '''Output 10 different states which remain unchanged
    '''

    return [
                [[1,1,0,0], [1,1,0,0], [0,0,0,0],[0,0,0,0]],
                [[0,1,1,0], [0,1,1,0], [0,0,0,0],[0,0,0,0]],
                [[0,0,1,1], [0,0,1,1], [0,0,0,0],[0,0,0,0]],
                [[0,0,0,0], [1,1,0,0], [1,1,0,0],[0,0,0,0]],
                [[0,0,0,0], [0,1,1,0], [0,1,1,0],[0,0,0,0]],
                [[0,0,0,0], [0,0,1,1], [0,0,1,1],[0,0,0,0]],
                [[0,0,0,0], [0,0,0,0], [0,0,0,0],[0,0,0,0]],
                [[0,0,0,0], [0,0,0,0], [1,1,0,0],[1,1,0,0]],
                [[0,0,0,0], [0,0,0,0], [0,1,1,0],[0,1,1,0]],
                [[0,0,0,0], [0,0,0,0], [0,0,1,1],[0,0,1,1]]
          ]

def mAp6(n=7):
    '''Output 2 states which return to them selves after at most 5 iterations
    '''
    return [
                [[0,0,0,0],[0,1,1,1],[1,1,1,0],[0,0,0,0]],
                [[0,1,0], [0,1,0], [0,1,0]]
           ]
def mAp7(A,k):
    '''Output the state of the matrix after k iterations if the
universe is a torus
    '''
    for i in xrange(0,k):
        mat = torus(A)
        isDead = 0
        for x in xrange(len(mat)-1):
            for y in xrange(len(mat)-1):
                isDead += mat[x][y]
        if isDead == 0:
            break
    return A

def torus(A):
    newA = matrix(A)
    for i in range(len(newA.rows())):
        for j in range(len(newA.columns())):
            cnt = 0
            L = []
            try:
                L.append(newA[i-1,j])        #UP
            except:
                L.append(newA.rows()[-1][j])

            try:
                if i-1 <= newA.nrows() and i-1 >= 0 and j+1 <= newA.ncols() and j+1 >= 0:        #right up
                    L.append(newA[i-1,j+1])
                else:    L.append(newA.rows()[-1][j+1])

            except:
                    L.append(newA.rows()[i-1][0])

            try:
                L.append(newA[i,j+1])        #right
            except:
                L.append(newA.columns()[0][i])

            try:
                if i+1 >= 0 and j+1 >= 0 :    #right down
                    L.append(newA[i+1,j+1])
                else:
                    L.append(newA.rows()[i+1][0])
            except:
                try:
                    L.append(newA.rows()[i+1][0])
                except:
                    try:
                        L.append(newA.rows()[0][j+1])
                    except:
                        L.append(newA.rows()[0][0])

            try:
                L.append(newA[i+1,j])        #down

            except:
                L.append(newA.columns()[j][0])

            try:
                if i+1 >= 0 and j-1 >= 0:    #down left
                    L.append(newA[i+1,j-1])
                else:
                    L.append(newA.columns()[-1][i+1])
            except:
                L.append(newA.columns()[j-1][0])

            try:                              #left
                    L.append(newA[i,j-1])
            except:
                L.append(L.append(newA.rows()[0][-1]))
            try:
                if i-1 >= 0 and j-1 >= 0:    # left up
                    L.append(newA[i-1,j-1])
                else:
                    L.append(newA.rows()[i-1][j-1])
            except:
                L.append(newA.rows()[-1][-1])

            for x in range(len(L)):
                if L[x] == 1:
                    cnt += 1

                if newA[i,j] == 1:
                    if cnt <= 1:
                        A[i][j] = 0
                    if cnt <= 4:
                        A[i][j] = 0
                    if cnt == 3 or cnt == 2:
                        A[i][j] = 1
                elif newA[i,j] == 0:
                    if cnt == 3:
                        A[i][j] = 1
                    else:
                        A[i][j] = 0
    return A


def mAp8(A,k):
    '''Output the state of the matrix after k iterations if the
universe is a Klein bottle
    '''
    for i in range(0,k):
        klein(A)
    return A

def klein(A):
    newA = matrix(A)
    for i in range(len(newA.rows())):
        for j in range(len(newA.columns())):
            cnt = 0
            L = []
            try:
                if i-1 >= 0 and j >= 0:
                    L.append(newA[i-1,j])        #UP
                else:
                    L.append(newA.rows()[-1][newA.ncols()-j-1])
            except:
                L.append(newA.rows()[-1][-1])

            try:
                if i-1 <= newA.nrows() and i-1 >= 0 and j+1 <= newA.ncols() and j+1 >= 0:        #right up
                    L.append(newA[i-1,j+1])
                else:    L.append(newA.rows()[-1][newA.ncols()-1-i])

            except:
                    L.append(newA.rows()[i-1][0])

            try:
                L.append(newA[i,j+1])        #right
            except:
                L.append(newA.columns()[0][i])

            try:
                if i+1 >= 0 and j+1 >= 0 :    #right down
                    L.append(newA[i+1,j+1])
                else:
                    L.append(newA.rows()[i+1][0])
            except:
                try:
                    L.append(newA.rows()[i+1][0])
                except:
                    try:
                        L.append(newA.rows()[0][j+1])
                    except:
                        L.append(newA.rows()[0][0])

            try:
                L.append(newA[i+1,j])        #down

            except:
                L.append(newA.columns()[j][0])

            try:
                if i+1 >= 0 and j-1 >= 0:    #down left
                    L.append(newA[i+1,j-1])
                else:
                    L.append(newA.columns()[-1][i+1])
            except:
                L.append(newA.columns()[j-1][0])

            try:                              #left
                    L.append(newA[i,j-1])
            except:
                L.append(L.append(newA.rows()[0][-1]))
            try:
                if i-1 >= 0 and j-1 >= 0:    # left up
                    L.append(newA[i-1,j-1])
                elif i-1 < 0 and j-1 < 0:
                    L.append(newA.rows()[-1][0])
                else:
                    L.append(newA.rows()[-1][newA.ncols()-j])
            except:
                L.append(newA.rows()[i-1][-1])

            for x in range(len(L)):
                if L[x] == 1:
                    cnt += 1

                if newA[i,j] == 1:
                    if cnt <= 1:
                        A[i][j] = 0
                    if cnt <= 4:
                        A[i][j] = 0
                    if cnt == 3 or cnt == 2:
                        A[i][j] = 1
                elif newA[i,j] == 0:
                    if cnt == 3:
                        A[i][j] = 1
                    else:
                        A[i][j] = 0
            #print L
    return A

