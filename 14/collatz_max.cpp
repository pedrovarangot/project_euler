#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

unordered_map<long long, int> collatz_length;

int do_a_collatz(long long n)
{
    if(n == 1) return 1;
    long long new_candidate;
    if(n % 2 == 0) {
        new_candidate = n / 2;
    } else {
        new_candidate = n * 3 + 1; 
    }
    auto found = collatz_length.find(new_candidate);
    if(found != collatz_length.end()) {
        collatz_length[n] = found->second + 1;
        return 1 + found->second;
    }  else {
        int rv = 1 + do_a_collatz(new_candidate);
        collatz_length[n] = rv;
        return rv;;
    }
}

int main() {
    int t;
    collatz_length[1] = 1;
    cin >> t;
  
    int biggest_result = 1;
    vector<int> old_results(5000001);
    for(int i = 0; i < 5000001; ++i) old_results[i] = -1;
    old_results[1] = 1;

    for(int a0 = 0; a0 < t; ++a0) {
        int n, this_chain_length, max_chain_length, the_starting_number;
        cin >> n;
        the_starting_number = old_results[min(biggest_result,n)];
        max_chain_length = collatz_length[min(biggest_result,n)];
        for(int i = biggest_result; i <= n; ++i) {
            auto found = collatz_length.find(i);
            if(found != collatz_length.end()) {
                this_chain_length = found->second;
            }  else {
                this_chain_length = do_a_collatz(i);
            }
            if(this_chain_length >= max_chain_length) {
                max_chain_length = this_chain_length;
                the_starting_number = i;
            }
            old_results[i] = the_starting_number;
            biggest_result = i;
        }
        cout << the_starting_number << endl;
    }
    
    return 0;
}
