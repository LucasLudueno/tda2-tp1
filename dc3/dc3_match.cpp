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
        std::cout << "Usage: dc3 <in text file> <pattern> <results>" << std::endl;
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
    std::vector<int> new_t = preprocess_string(t, k);
    std::vector<int> suffix_array = dc3(new_t, k);
    std::string p = argv[2];
    std::vector<int> results = search(suffix_array, t, p);
    std::ofstream results_file (argv[3]);
    for (int i = 0; i < results.size(); i++) {
        results_file << results[i] << std::endl;
    }

}
