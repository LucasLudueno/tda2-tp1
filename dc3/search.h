#ifndef NEW_VERSION_SEARCH_H
#define NEW_VERSION_SEARCH_H

#include <vector>
#include <string>
int _search(const std::vector<int> &d, const std::string &t, const std::string &p, int l, int r);

std::vector<int> search(const std::vector<int> &d, const std::string &t, const std::string &p);

std::vector<int> search2(const std::vector<int> &suffix_array, const std::string &t, const std::string &p);

#endif //NEW_VERSION_SEARCH_H
