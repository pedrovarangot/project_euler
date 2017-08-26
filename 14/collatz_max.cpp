#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

unordered_map<int, int> collatz_length;

int do_a_collatz(int n)
{
    //cout << "doing " << n << endl;
    int acum = 1;
    long long new_candidate = n;
    while(new_candidate != 1) {
        acum++;
        if(new_candidate % 2 == 0) {
            new_candidate = new_candidate / 2;
        } else {
            new_candidate = new_candidate * 3 + 1; 
        }
        //cout << new_candidate << " ";
        if(collatz_length.find(new_candidate) != collatz_length.end()) {
            //cout << " + length " << new_candidate << endl;
            collatz_length[n] = acum + collatz_length[new_candidate];
            return acum + collatz_length[new_candidate];
        }
    }
    collatz_length[n] = acum;
    return acum;
}

int main() {
    int t;
    collatz_length[1] = 1;
    cin >> t;
    
    for(int a0 = 0; a0 < t; ++a0) {
        int n, this_chain_length, max_chain_length, the_starting_number;
        cin >> n;
        the_starting_number = 1;
        max_chain_length = 1;
        for(int i = 1; i <= n; ++i) {
            if(collatz_length.find(i) != collatz_length.end()) {
                this_chain_length = collatz_length[i];
            }  else {
                this_chain_length = do_a_collatz(i);
            }
            if(this_chain_length >= max_chain_length) {
                max_chain_length = this_chain_length;
                the_starting_number = i;
            }
        }
        cout << the_starting_number << endl;
    }
    
    return 0;
}
