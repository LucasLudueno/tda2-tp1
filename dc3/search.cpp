#include <vector>
#include <string>
#include <algorithm>
#include <iostream>

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

std::vector<int> search2(const std::vector<int> &suffix_array, const std::string &t, const std::string &p) {
    // En vez de buscar el primer match, y después recorrer a ambos lados linealmente para encontrar todos los matches,
    // como en "search", acá buscamos primero el inicio del intervalo de los matches, y después el final del intervalo.
    // Son sólo dos búsquedas binarias.
    int n = t.size() - 1;
    int l = 0;
    int r = n;
    int mid;
    while (l < r) {
        // Con esto buscamos el inicio del intervalo
        mid = (l + r) / 2;
        if (p > t.substr(suffix_array[mid], p.size())) {
            // Si p es mayor, nos quedamos con la parte derecha
            l = mid + 1;
        } else {
            // Si es menor o igual, nos quedamos con la parte izquierda
            r = mid;
        }
    }
    int s = l;
    r = n;
    while (l < r) {
        // Con esto buscamos el final del intervalo
        mid = (l + r) / 2;
        if (p < t.substr(suffix_array[mid], p.size())) {
            // Si es menor o igual, nos quedamos con la parte izquierda
            r = mid;
        } else {
            // Si p es mayor, nos quedamos con la parte derecha
            l = mid + 1;
        }
    }
    std::vector<int> result(suffix_array.begin() + s, suffix_array.begin() + r);
    std::sort(result.begin(), result.end());
    return result;


}