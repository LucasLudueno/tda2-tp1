#include <iostream>
#include "dc3.h"

void radix_pass(std::vector<int> &c, std::vector<int> &t, int pos, int k) {
    std::vector<int> counters(k, 0); // Contadores para cada caracter en cero
    std::vector<int> sorted; // En sorted cada posición de sorted pongo el índice dentro de c? que van en esa posición, según el orden
    for (int i = 0; i < c.size(); i++) {
        int ch;
        if (c[i] + pos > t.size() - 1) {
            ch = 0;
        } else {
            ch = t[c[i] + pos];
        }
        counters[ch]++;
    }

    int total = 0;
    for (int i = 0; i < counters.size(); i++) {
        int old_counter = counters[i]; // Reemplazo cada contador por la posición en la que voy a empezar a poner (ordenados)
        // los elementos de r que están en ese counter (que tienen el 3er digito igual a i)
        counters[i] = total;
        total += old_counter;
    }

    // del 3er dígito
    for (int i = 0; i < c.size(); i++) {
        sorted.push_back(0);
    }
    for (int i = 0; i < c.size(); i++) {
        int ch;
        if (c[i] + pos > t.size() - 1) {
            ch = 0;
        } else {
            ch = t[c[i] + pos];
        }
        sorted[counters[ch]] = c[i];
        counters[ch]++; // Avanzo la posición para el próximo elemento que este en este contador
    }
    for (int i = 0; i < c.size(); i++) {
        c[i] = sorted[i];
    }

}

void build_rank(std::vector<int> &r_sorted, std::vector<int> &c, std::vector<int> &t, bool &has_duplicates,
                std::vector<int> &rank) {
    int current_rank = 1;
    std::vector<int> pos_in_c(t.size());
    for (int i = 0; i < c.size(); i++) {
        pos_in_c[c[i]] = i;
    }
    has_duplicates = false;
    for (int i = 0; i < c.size(); i++) {
        if (i >= 1) {
            if (t[r_sorted[i]] == t[r_sorted[i - 1]] && t[r_sorted[i] + 1] == t[r_sorted[i - 1] + 1] &&
                t[r_sorted[i] + 2] == t[r_sorted[i - 1] + 2]) {
                has_duplicates = true;
                // No avanzar el rank, porque es igual al anterior
            } else {
                // Si es distinto al anterior, avanzar el rank
                current_rank++;
            }
        }
        rank[pos_in_c[r_sorted[i]]] = current_rank;
    }
}

void sort_samples(std::vector<int> &t, int k, std::vector<int> &sorted_samples, std::vector<int> &rank) {
    std::vector<int> c; // Vector que contiene los indices de los sufijos que comienzan en posiciones no múltiplos de 3
    int j = 0;
    // Inicializo c
    for (int i = 0; i < t.size(); i++) {
        if (i % 3 == 1) {
            //c[j++] = i;
            c.push_back(i);
        }
    }
    for (int i = 0; i < t.size(); i++) {
        if (i % 3 == 2) {
            //c[j++] = i;
            c.push_back(i);
        }
    }

    std::vector<int> r_sorted(c);

    radix_pass(r_sorted, t, 2, k); // Ordenar por el 3er dígito
    radix_pass(r_sorted, t, 1, k); // Ordenar por el 2do dígito
    radix_pass(r_sorted, t, 0, k); // Ordenar por el 1er dígito

    bool has_duplicates;
    std::vector<int> r_prime(r_sorted.size(), 0);
    build_rank(r_sorted, c, t, has_duplicates, r_prime); // Construir el rank, y ver si hay duplicados

    if (!has_duplicates) {
        // No hay duplicados, el suffix array es el mismo r_prim
        sorted_samples = r_sorted;
    } else {
        // Hay duplicados, llamar recursivamente a dc3 con el rank como string
        std::vector<int> sa_r_prime = dc3(r_prime, r_prime.size());
        int j = 0;
        sorted_samples = std::vector<int>(c.size());
        for (int i = 0; i < sa_r_prime.size(); ++i) {
            if (sa_r_prime[i] < c.size()) {
                sorted_samples[j++] = c[sa_r_prime[i]];
            }
        }
    }
    rank = std::vector<int>(t.size() + 2, -1);
    rank[rank.size() - 1] = 0;
    rank[rank.size() - 2] = 0;
    for (int i = 0; i < sorted_samples.size(); ++i) {
        rank[sorted_samples[i]] = i;
    }
}

void sort_non_samples(std::vector<int> &t, int k, std::vector<int> &sorted_non_samples, std::vector<int> &rank) {
    for (int i = 0; i < t.size(); ++i) {
        if (i % 3 == 0) {
            sorted_non_samples.push_back(i);
        }
    }
    radix_pass(sorted_non_samples, rank, 1, rank.size()); // Ordenar por rank del sufijo siguiente
    radix_pass(sorted_non_samples, t, 0, k); // Ordenar por primer dígito
}

int comp(int i, int j, std::vector<int> &t, std::vector<int> &rank) {
    if (j % 3 == 1) {

        return (t[i] > t[j]) || (t[i] == t[j] && rank[i + 1] > rank[j + 1]);
    } else if (j % 3 == 2) {
        int x = t.size();
        int c0;
        int c1;
        if (i + 1 >= x) {
            c0 = 0;
        } else {
            c0 = t[i + 1];
        }
        if (j + 1 >= x) {
            c1 = 0;
        } else {
            c1 = t[j + 1];
        }
        return (t[i] > t[j]) || (t[i] == t[j] && c0 > c1) || (t[i] == t[j] && c0 == c1 && rank[i + 2] > rank[j + 2]);
    }
}


std::vector<int> merge(std::vector<int> &t, std::vector<int> &sorted_non_samples, std::vector<int> &sorted_samples,
                       std::vector<int> &rank) {
    int i = 0;
    int j = 0;

    int l_s_n_s = sorted_non_samples.size();
    int l_s_s = sorted_samples.size();
    std::vector<int> result(l_s_n_s + l_s_s);
    int m = 0;
    while (i < l_s_n_s && j < l_s_s) {
        int a = sorted_non_samples[i];
        int b = sorted_samples[j];
        if (comp(a, b, t, rank) > 0) {
            result[m] = sorted_samples[j];
            m++;
            j += 1;
        } else {
            result[m] = sorted_non_samples[i];
            m++;
            i += 1;
        }
    }
    if (i == sorted_non_samples.size()) {
        for (int k = j; k < sorted_samples.size(); k++) {
            result[m] = sorted_samples[k];
            m++;
        }
    }
    if (j == sorted_samples.size()) {
        for (int k = i; k < sorted_non_samples.size(); k++) {
            result[m] = sorted_non_samples[k];
            m++;
        }
    }
    return result;
}

std::vector<int> dc3(std::vector<int> &t, int k) {

    std::vector<int> sorted_samples;
    std::vector<int> rank;
    std::vector<int> sorted_non_samples;
    sort_samples(t, k, sorted_samples, rank);
    sort_non_samples(t, k, sorted_non_samples, rank);
    return merge(t, sorted_non_samples, sorted_samples, rank);
}