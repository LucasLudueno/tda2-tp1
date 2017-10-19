#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include "dc3.h"
#include "search.h"

std::vector<int> preprocess_string(std::string &t, int &k) {
    std::vector<int> new_t(t.size());
    int min = 1000000; // Ver qué poner acá
    int max = -1;
    for (int i = 0; i < t.size(); ++i) {
        // Busco el mínimo y el máximo caracter en el texto
        int ch = (int) t[i] + 128;
        if (ch < min) {
            min = ch;
        }
        if (ch > max) {
            max = ch;
        }
    }
    std::vector<int> mmm(max + 1);
    // Marco cuáles de los caracteres en el rango min, max aparecen en el texto
    for (int i = 0; i < t.size(); ++i) {
        mmm[(int) t[i] + 128]++;
    }
    int current = 1;
    // Reemplazo en el texto cada caracter por su ranking entre los caracteres que hay en el texto
    for (int i = 0; i < mmm.size(); ++i) {
        if (mmm[i] != 0) {
            mmm[i] = current;
            current++;
        }
    }
    k = current;
    for (int i = 0; i < t.size(); ++i) {
        new_t[i] = mmm[(int) t[i] + 128];
    }
    return new_t;
}

int main(int argc, char *argv[]) {
    if (argc < 3) {
        std::cout << "Usage: dc3 <in text file> <out sa file>" << std::endl;
        return 0;
    }
    std::ifstream file(argv[1]);
    if (!file.is_open()) {
        std::cerr << "Could not open file \"" << argv[1] << "\"" << std::endl;
        return -1;
    }
    std::stringstream buffer;
    buffer << file.rdbuf();
    std::string t;
    t = buffer.str();
    int k;
    clock_t s, e;
    s = clock();
    std::vector<int> new_t = preprocess_string(t, k);
    e = clock();
    std::cout << "Time to preprocess string = " << ((double) (e - s)) / CLOCKS_PER_SEC << " s" << std::endl;
    s = clock();
    std::vector<int> suffix_array = dc3(new_t, k);
    e = clock();
    std::cout << "Time to build suffix array = " << ((double) (e - s)) / CLOCKS_PER_SEC << " s" << std::endl;
    std::ofstream sa_file(argv[2]);
    for (int i = 0; i < suffix_array.size(); ++i) {
        sa_file << suffix_array[i] << std::endl;
    }
    std::string p;
    std::cout << "Pattern to search:";
    std::getline(std::cin, p);
    while (p != "") {
        s = clock();
        std::vector<int> results = search2(suffix_array, t, p);
        e = clock();
        std::cout << "Time to search pattern = " << ((double) (e - s)) / CLOCKS_PER_SEC << " s" << std::endl;
        std::cout << "Found " << results.size() << " matches" << std::endl;
        std::cin.get();
        for (int i = 0; i < results.size(); i++) {
            std::cout << "[" << results[i] << "] " << t.substr(results[i], p.size() + 50) << std::endl;
        }
        std::cout << "Pattern to search:";
        std::getline(std::cin, p);
    }
}
