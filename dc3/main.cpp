#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include "dc3.h"
#include "search.h"

std::vector<int> prepare_string(std::string& t, int& k){
    std::vector<int> new_t(t.size());
    int min = 1000000; // Ver qué poner acá
    int max = -1;
    for (int i = 0; i < t.size(); ++i) {
        // Busco el mínimo y el máximo caracter en el texto
        int ch = (int)t[i];
        if (ch < min){
            min = ch;
        }
        if (ch > max){
            max = ch;
        }
    }

    std::vector<int> mmm(max+1);
    // Marco cuáles de los caracteres en el rango min, max aparecen en el texto
    for (int i = 0; i < t.size(); ++i) {
        mmm[t[i]]++;
    }
    int current = 1;
    // Reemplazo en el texto cada caracter por su ranking entre los caracteres que hay en el texto
    for (int i = 0; i < mmm.size(); ++i) {
        if (mmm[i] != 0){
            mmm[i] = current;
            current++;
        }
    }
    k = current;
    for (int i = 0; i < t.size(); ++i) {
        new_t[i] = mmm[t[i]];
    }
    return new_t;
}

int main(int argc, char* argv[]) {
    if (argc < 2){
        std::cout << "Usage: dc3 <file>" << std::endl;
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
    std::vector<int> new_t = prepare_string(t,k);
    std::vector<int> suffix_array = dc3(new_t, k);
    std::string p;
    std::cout << "Pattern to search:";
    std::getline(std::cin,p);
    while(p != ""){
        std::vector<int> results = search(suffix_array,t,p);
        std::cout << "Found " << results.size() << " matches" << std::endl;
        std::cin.get();
        for(int i = 0; i < results.size(); i++){
            std::cout << "[" << results[i] << "] "<< t.substr(results[i],p.size()+50) << std::endl;
        }
        std::cout << "Pattern to search:";
        std::getline(std::cin,p);
    }
}