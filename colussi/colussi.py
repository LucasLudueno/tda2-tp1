def pre_colussi(x, m):
    hmax = compute_hmax(x, m)
    kmin = compute_kmin(m, hmax)
    rmin = compute_rmin(m, hmax, kmin)
    h,nd = compute_h(m,kmin)
    shift = compute_shift(m, kmin, rmin, nd, h)
    nhdo = compute_nhdo(m,kmin)
    next = compute_next(m,rmin, kmin, nd,nhdo,h)
    return h, nd, shift, next

def compute_hmax(x, m):
    # hmax[k] is such that x[k..hmax[k]-1] = x[0..hmax[k]- k - 1]
    i = 1
    k = 1
    hmax = [0] * (m + 1)
    while True:
        while x[i] == x[i - k]:
            i += 1
        hmax[k] = i
        q = k + 1
        while hmax[q-k] + k < i:
            hmax[q] = hmax[q - k] + k
            q += 1
        k = q
        if k == i + 1:
            i = k
        if k > m:
            break
    return hmax


def compute_kmin(m, hmax):
    kmin = [0] * (m + 1)
    for i in range(m, 0, -1):
        if hmax[i] < m:
            kmin[hmax[i]] = i
    return kmin


def compute_rmin(m, hmax, kmin):
    rmin = [0] * (m + 1)
    r = 0
    for i in range(m-1, -1, -1):
        if hmax[i+1] == m:
            r = i + 1
        if kmin[i] == 0:
            rmin[i] = r
        else:
            rmin[i] = 0
    return rmin


def compute_h(m, kmin):
    h = [0] * (m+1)
    s = -1
    r = m
    for i in range(0,m,1):
        if kmin[i] == 0:
            r -= 1
            h[r] = i
        else:
            s += 1
            h[s] = i
    nd = s
    return h, nd


def compute_shift(m, kmin, rmin, nd, h):
    shift = [0] * (m+1)
    for i in range(0, nd+1, 1):
        shift[i] = kmin[h[i]]
    for i in range(nd + 1, m, 1):
        shift[i] = rmin[h[i]]
    shift[m] = rmin[0]
    return shift

def compute_nhdo(m, kmin):
    nhdo = [0] * (m+1)
    s = 0
    for i in range(0, m, 1):
        nhdo[i] = s
        if kmin[i] > 0:
            s += 1
    return nhdo

def compute_next(m, rmin, kmin, nd, nhdo, h):
    next = [0]*(m+1)
    for i in range(0, nd+1, 1):
        next[i] = nhdo[h[i] - kmin[h[i]]]
    for i in range(nd + 1, m, 1):
        next[i] = nhdo[m - rmin[h[i]]]
    next[m] = nhdo[m - rmin[h[m-1]]]
    return next

def colussi(T, P):
    i = j = last = nd = 0
    h = next = shift = []
    n = len(T)
    m = len(P)
    P = P + '\0'
    
    h, nd, shift, next = pre_colussi(P,m)
    result = []
    last = -1
    while j <= n - m:
        while i < m and last < j + h[i] and P[h[i]] == T[j + h[i]]:
            i += 1
        if i >= m or last >= j + h[i]:
            result.insert(len(result),j)
            i = m
        if i > nd:
            last = j + m - 1
        j += shift[i]
        i = next[i]

    return result

class Colussi:
    def __init__(self, text):
        self.text = text

    def match(self, pattern):
        return colussi(self.text, pattern)

    def name(self):
        return "Colussi"
