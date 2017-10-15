#include <vector>
#include <string>
#include <algorithm>

int _search(const std::vector<int> &d, const std::string &t, const std::string &p, int l, int r) {
    if (l > r) {
        return -1;
    }
    int m = (l + r) / 2;
    int s = d[m];
    if (t.substr(s, p.size()) > p) {
        r = m - 1;
        return _search(d, t, p, l, r);
    } else if (t.substr(s, p.size()) == p) {
        return m;
    } else {
        l = m + 1;
        return _search(d, t, p, l, r);
    }
}

std::vector<int> search(const std::vector<int> &d, const std::string &t, const std::string &p) {
    int j = _search(d, t, p, 0, d.size() - 1);
    if (j == -1) {
        return std::vector<int>();
    }
    std::vector<int> r;
    int s = d[j];
    int m = j;
    while (s >= 0 && t.substr(s, p.size()) == p) {
        r.push_back(s);
        if (m == 0) {
            break;
        }
        m -= 1;
        s = d[m];
    }
    j += 1;
    if (j >= d.size()) {
        // Ordeno por posición
        std::sort(r.begin(), r.end());
        return r;
    }
    s = d[j];
    m = j;
    while (s >= 0 && t.substr(s, p.size()) == p) {
        r.push_back(s);
        if (m == d.size() - 1) {
            break;
        }
        m += 1;
        s = d[m];
    }
    // Ordeno por posición
    std::sort(r.begin(), r.end());
    return r;
}