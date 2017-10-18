#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>

int main(int argc, char *argv[]) {
    if (argc < 4) {
        std::cout << "Usage: lcp <in text file> <in sa file> <out lcp file>" << std::endl;
        return 0;
    }

    std::ifstream text_file(argv[1]);
    if (!text_file.is_open()) {
        std::cerr << "Could not open text_file \"" << argv[1] << "\"" << std::endl;
        return -1;
    }

    std::stringstream buffer;
    buffer << text_file.rdbuf();
    std::string t;
    t = buffer.str();
    std::ifstream sa_file(argv[2]);
    if (!sa_file.is_open()) {
        std::cerr << "Could not open sa_file \"" << argv[1] << "\"" << std::endl;
        return -1;
    }

    std::ofstream lcp_file(argv[3]);
    if (!sa_file.is_open()) {
        std::cerr << "Could not open lcp_file \"" << argv[1] << "\"" << std::endl;
        return -1;
    }

    std::vector<int> suffix_array(t.size(), 0);
    for (int i = 0; i < t.size(); i++) {
        sa_file >> suffix_array[i];
    }

    std::vector<int> suffix_array_inv(suffix_array.size());
    for (int i = 0; i < suffix_array.size(); i++) {
        suffix_array_inv[suffix_array[i]] = i;
    }
    std::vector<int> lcp(suffix_array.size(),-1);
    int l = 0;
    clock_t s,e;
    s = clock();
    for (int i = 0; i < lcp.size(); i++) {
        int k = suffix_array_inv[i];
        if (k >= 1) {
            int j = suffix_array[k - 1];
            while (t[i + l] == t[j + l]) {
                l++;
            }
            lcp[k] = l;
            if (l > 0) {
                l--;
            };
        }
    }
    e = clock();
    std::cout << "Time to build lcp = " << ((double) (e - s)) / CLOCKS_PER_SEC << " s" << std::endl;
    for (int i = 0; i < lcp.size(); i++) {
        lcp_file << lcp[i] << std::endl;
    }
}