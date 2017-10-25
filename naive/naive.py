def naive (text, pattern):
    n = len(text)
    m = len(pattern)
    result = []
    for j in range(0,n - m + 1):
        i = 0
        while i < m and text[i+j] == pattern[i]:
            i += 1
        if i == m:
            result.append(j)
    return result

class Naive:
    def __init__(self, text):
        self.text = text

    def match(self, pattern):
        return naive(self.text, pattern)

    def name(self):
        return "Naive"