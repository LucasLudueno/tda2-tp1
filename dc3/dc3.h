#ifndef NEW_VERSION_DC3_H
#define NEW_VERSION_DC3_H

#include <vector>
#include <set>
#include <map>

#include "dc3.h"

void radix_pass(std::vector<int> &c, std::vector<int> &t, int pos, int k);

void build_rank(std::vector<int> &r_sorted, std::vector<int> &c, std::vector<int> &t, bool &has_duplicates,
                std::vector<int> &rank);
void sort_samples(std::vector<int> &t, int k, std::vector<int> &sorted_samples, std::vector<int> &rank);

void sort_non_samples(std::vector<int> &t, int k, std::vector<int> &sorted_non_samples, std::vector<int> &rank);

int comp(int i, int j, std::vector<int> &t, std::vector<int> &rank);

std::vector<int> merge(std::vector<int> &t, std::vector<int> &sorted_non_samples, std::vector<int> &sorted_samples,
                       std::vector<int> &rank);

std::vector<int> dc3(std::vector<int> &t, int k);

#endif //NEW_VERSION_DC3_H
