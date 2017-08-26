#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

//unordered_map<long long, int> collatz_length;
#define MAX 10000000
vector<int> collatz_length_v(MAX);

int do_a_collatz(long long n)
{
    if(n == 1) return 1;
    long long new_candidate;
    if(n % 2 == 0) {
        new_candidate = n / 2;
    } else {
        new_candidate = n * 3 + 1; 
    }
    //auto found = collatz_length.find(new_candidate);
    bool found = new_candidate < MAX && collatz_length_v[new_candidate] != -1;
    if(found /*!= collatz_length.end()*/) {
        int rv = collatz_length_v[new_candidate] + 1;
        if(n < MAX) collatz_length_v[n] = rv;
        return rv;
    }  else {
        int rv = 1 + do_a_collatz(new_candidate);
        if(n < MAX) collatz_length_v[n] = rv;
        return rv;
    }
}

int main() {
    int t;
    for(int i = 0; i < MAX; ++i) collatz_length_v[i] = -1;
    collatz_length_v[1] = 1;
    cin >> t;
  
    int biggest_result = 1;
    vector<int> old_results(5000001);
    for(int i = 0; i < 5000001; ++i) old_results[i] = -1;
    old_results[1] = 1;

    for(int a0 = 0; a0 < t; ++a0) {
        int n, this_chain_length, max_chain_length, the_starting_number;
        cin >> n;
        the_starting_number = old_results[min(biggest_result,n)];
        max_chain_length = collatz_length_v[old_results[min(biggest_result,n)]];
        for(int i = biggest_result; i <= n; ++i) {
            //auto found = collatz_length.find(i);
            if(collatz_length_v[i] != -1/*found != collatz_length.end()*/) {
                this_chain_length = collatz_length_v[i];
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
