class DC3(object):
    def __init__(self, t):
        self.t = t
        self.suffix_array = self.dc3(t)

    def dc3(self, t):
        old_t = t
        t = list(t)
        x, t = self.to_ints(t)
        new_t = t
        rank, sorted_samples = self.sort_samples(t, x)
        sorted_non_samples = self.sort_non_samples(t, rank)
        return self.merge(t, sorted_non_samples, sorted_samples, rank)

    def to_ints(self, t):
        x = list(set(t))
        x.sort()
        # x = sorted(set(t))

        x = {x[i]: i for i in range(len(x))}
        t = [x[i] + 1 for i in t]
        t.append(0)
        return x, t

    def sort_samples(self, t, x):
        # Construct a sample
        b1 = [i for i in range(len(t)) if i % 3 == 1]
        b2 = [i for i in range(len(t)) if i % 3 == 2]
        c = b1 + b2

        r = [tuple(t[i:i + 3]) for i in c]
        # r_prim = sorted(set(r))
        r_prim = list(set(r))
        r_prim.sort()
        _map = {r_prim[i]: i for i in range(len(r_prim))}
        # Reemplazo cada "caracter" con su ranking dentro de r ordenado
        r_prim = [_map[x] + 1 for x in r]
        _map = {r_prim[i]: i for i in range(len(r_prim))}

        # Si no tiene duplicados, ya está
        if len(r_prim) == len(set(r_prim)):
            sorted_samples = [c[_map[i + 1]] for i in range(len(c))]
        # Si tiene duplicados, recursivamente
        else:
            sa_r_prim = self.dc3(r_prim)
            sorted_samples = [0 for _ in c]
            j = 0
            for i in range(len(sa_r_prim)):
                if sa_r_prim[i] < len(c):
                    sorted_samples[j] = c[sa_r_prim[i]]
                    j += 1

        rank = [None] * (len(t) + 2)
        rank[-2:] = [0, 0]
        _map = {sorted_samples[i]: i for i in range(len(sorted_samples))}
        for i in sorted_samples:
            rank[i] = _map[i] + 1
        return rank, sorted_samples

    def sort_non_samples(self, t, rank):
        sorted_non_samples = [(t[i], rank[i + 1], i) for i in range(len(t)) if i % 3 == 0]
        # El "i" que está en la tercera posición no se usa para ordenar

        # sorted_non_samples = sorted(sorted_non_samples)
        sorted_non_samples.sort()
        # Me quedo sólo con los índices ordenados, el resto no lo necesito por ahora
        sorted_non_samples = [x[2] for x in sorted_non_samples]
        return sorted_non_samples

    def comp(self, i, j, t, rank):
        if j % 3 == 1:
            return (t[i], rank[i + 1]) > (t[j], rank[j + 1])
        elif j % 3 == 2:
            x = len(t)
            if i + 1 >= x:
                c0 = 0
            else:
                c0 = t[i + 1]
            if j + 1 >= x:
                c1 = 0
            else:
                c1 = t[j + 1]
            return (t[i], c0, rank[i + 2]) > (t[j], c1, rank[j + 2])

    def merge(self, t, sorted_non_samples, sorted_samples, rank):

        i = 0
        j = 0
        result = []
        l_s_n_s = len(sorted_non_samples)
        l_s_s = len(sorted_samples)
        while i < l_s_n_s and j < l_s_s:
            a = sorted_non_samples[i]
            b = sorted_samples[j]
            if self.comp(a, b, t, rank) > 0:  # a > b
                result.append(sorted_samples[j])
                j += 1
            else:
                result.append(sorted_non_samples[i])
                i += 1
        if i == len(sorted_non_samples):
            result += sorted_samples[j:]
        if j == len(sorted_samples):
            result += sorted_non_samples[i:]
        return result

    def _search(self,suffix_array, t, p, l, r):
        if l > r:
            return -1
        m = (l + r) // 2
        s = self.suffix_array[m]
        if t[s:s + len(p)] > p:
            r = m - 1
            return self._search(self.suffix_array, t, p, l, r)
        elif t[s:s + len(p)] == p:
            return m
        else:
            l = m + 1
            return self._search(self.suffix_array, t, p, l, r)


    def search(self,p):

        j = self._search(self.suffix_array, self.t, p, 0, len(self.suffix_array) - 1)
        if j == -1:
            return []
        r = []
        # Search backwards in self.suffix_array
        s = self.suffix_array[j]
        m = j
        while s >= 0 and self.t[s:s + len(p)] == p:
            r.append(s)
            if m == 0:
                break
            m -= 1
            s = self.suffix_array[m]
        # Search forward in self.suffix_array
        j += 1
        if j >= len(self.suffix_array):
            return r
        s = self.suffix_array[j]
        m = j
        while s >= 0 and self.t[s:s + len(p)] == p:
            r.append(s)
            if m == len(self.suffix_array) - 1:
                break
            m +=1
            s = self.suffix_array[m]
        return r