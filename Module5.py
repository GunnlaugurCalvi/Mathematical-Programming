def m5p1(G):
    '''Return the size of the largest clique
    '''

    p = MixedIntegerLinearProgram()
    v = p.new_variable(nonnegative = True, binary = True)

    vrt = [i for i in G.keys()]
    n = [j for j in G.values()]

    p.set_objective(sum(v[g] for g in G))

    for i in range(len(vrt)):
        for j in range(i+1, len(vrt)):
            if vrt[i] not in n[j]:
                p.add_constraint(v[i] + v[j], max=1)
    return p.solve()

def m5p2(G):
    '''Return the size of the largest independent set
    '''
    p = MixedIntegerLinearProgram()
    v = p.new_variable(nonnegative = True, binary = True)

    vrt = [i for i in G.keys()]
    n = [j for j in G.values()]

    p.set_objective(sum(v[g] for g in G))

    for i in range(len(vrt)):
        for j in range(i+1, len(vrt)):
            if vrt[i] in n[j]:
                p.add_constraint(v[i] + v[j], max=1)
    return p.solve()

def m5p3(U, S):
    '''Return the lowest number of subsets from S to cover U
    '''

#     return len(set(Combinations(U,S)))

def m5p4(xmin, xmax, ymin, ymax):
    '''Return a lambda function for the square bounded by xmin-xmax and ymin-ymax
    '''
    return lambda px, py: (xmin <= px <= xmax and ymin <= py <= ymax)

def m5p5(x0, y0, r):
    '''Return a lambda function for the square with center (x0, y0) and side length 2r
    '''
    return lambda px, py: (x0 - r) <= px <= (x0 + r) and (y0 - r) <= py <= (y0 + r)

def m5p6(x0, y0, r):
    '''Return a lambda function for the disc with center (x0, y0) and radius r
    '''
    return lambda px, py: (x0 - px)**2 + (y0 - py)**2 <= r**2

def m5p7((a0, b0, r), n=1000, xmin=-1, xmax=1, ymin=-1, ymax=1):
    '''Return an approximation of the area covered by P (a disc) inside the rectangle
    '''
    return hits(m5p6(a0,b0,r), n, xmin, xmax, ymin, ymax)


def hits(P, n=1000, xmin=-1, xmax=1, ymin=-1, ymax=1):
    out = []
    area = (xmin - xmax) * (ymin - ymax) #area of rectangle
    for i in xrange(n):
        x = random() * (xmax - xmin) + xmin
        y = random() * (ymax - ymin) + ymin
        if P(x, y):
            out.append((x, y))

    return float(round((len(out) / n) * area,1))
# D = m5p6(0,0,1) # The unit disk
# R = points(hits(D))
# #R.show()

def m5p8(f, n=1000, xmin=-1, xmax=1, ymin=-1, ymax=1, zmax=1):
    '''Return an approximation of the volume between the function and the xy-plane
    '''
    return -1

