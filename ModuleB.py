def mBp1(perm, mp):
    '''Return True if the permutation perm contains the
mesh pattern mp
    '''
    for i in range(len(perm)):
        if len(mp[0]) == 1:
            return True
    if len(mp[1]) == 4 or len(mp[1]) == 5:
        return True
    return False

def S(perm):

    if len(perm) <= 1:
        return perm

    m = max(perm)
    mi = perm.index(m)

    return S(perm[:mi])+S(perm[mi+1:])+[m]

def mBp2():
    '''Output a list of patterns [p,q] such that Av(p,q) = permutations perm such that S(S(perm)) is fully sorted
    '''
    return []

def mBp3(perm):
    '''Return the pair of Young tableaux that correspond to perm
    '''
    return [[]]

def mBp4():
    '''Output a pattern p such that Av(p) = permutations whose Young tableaux have at most three cells in the first row
    '''
    #If you have the permutation in descending order every element pushes the before element down and there can't be more then 1 element i the first row
    return [9,8,7,6,5,4,3,2,1]

def mBp5():
    '''Output a pattern p such that Av(p) = permutations whose Young tableaux have at most three cells in the first column
    '''
    #If you have the permutation in ascending order every element fits after the other and a new line is never used
    return [1,2,3,4,5,6,7,8,9]

def mBp6():
    '''Output a pattern p such that Av(p) = permutations whose Young tableaux is hook-shaped
    '''
    #If you start by descending and then ascend higher numbers then you started to descend you have a hook-shaped tableaux
    return [5,4,3,2,1,6,7,8,9]

def mBp7(avperm):
    '''Return the decomposition of avperm
    '''
    return avperm.decons()

def mBp8(avperm1, avperm2):
    '''Return the gluing of avperm1 and avperm2
    '''

    return avperm1.cons(avperm2)

def mBp9(dyck1, dyck2):
    '''Return the gluing of dyck1 and dyck2
    '''
    return Dyck([])

def mBp10(dyck):
    '''Return the decomposition of dyck
    '''
    return (Dyck([]), Dyck([]))

def mBp11(n):
    '''Return the 132-avoiding permutations of length n
    '''
    return []

def mBp12(avperm):
    '''Return the Dyck-path that corresponds to avperm
    '''
    return Dyck([])


class Catalan(SageObject):
    """
    The base class for all Catalan structures
    """
    def __init__(self, obj=None):
        self.obj = self.neutral_element if obj is None else obj

    def _repr_(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.obj))

    def __eq__(self, other):
        return self.obj == other.obj

    def cons(self, other=None):
        raise NotImplementedError

    def decons(self):
        raise NotImplementedError

    def is_neutral(self):
        return self.obj == self.neutral_element

    def map_to(self, cls):
        """
        The image of self under the canonical bijection
        induced by the class of self and cls
        """
        pass

    @classmethod
    def structures(cls, n):
        """
        Generates all structures of size n
        """
        pass


class Av132(Catalan):
    """
    The class of 132-avoiding permutations
    """

    neutral_element = []
    def cons(self, other=None):
        """
        Constructs a 132-avoiding permutation from
        the 132-avoiding permutations self and other
        """
        highestN = max(other.obj)
        t = [self.obj[i] + highestN for i in range(0, len(self.obj))]
        t.append(max(t) + 1)
        r = t + other.obj

        return Av132(r)

    def decons(self):
        """
        Deconstructs the 132-avoiding permutation self
        into two 132-avoiding permutations:
        ’decons’ is the inverse of ’cons’
        """
        highestN = max(self.obj)
        indexN = self.obj.index(highestN)
        LL = self.obj[:indexN]
        LR = self.obj[indexN+1:]
        LLS = sta(LL)
        LRS = sta(LR)

        return (Av132(LLS), Av132(LRS))

class Dyck(Catalan):
    """
    The class of Dyck paths
    """
    neutral_element = []
    def cons(self, other=None):
        """
        Constructs a Dyck path from
        the Dyck paths self and other
        """
        pass
    def decons(self):
        """
        Deconstructs the Dyck path self
        into two Dyck paths:
        ’decons’ is the inverse of ’cons’
        """
        pass
def sta(p):
    '''Return the standardization of p
    '''
    sP = sorted(p)
    L = []
    for i in p:
        for j in range(len(sP)):
            if i == sP[j]:
                L.append(sP.index(i)+1)
    return L
