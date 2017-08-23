#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int cases;
    
    cin >> cases;
    for(int i = 0; i < cases; ++i) {
        int max;
        cin >> max;
        long sum = 0;
        for(int j = 0; j < max; j += 3) {
            sum += j;
        }
        for(int j = 0; j < max; j += 5) {
            sum += j;
        }
        for(int j = 0; j < max; j += 15) {
            sum -= j;
        }
        cout << sum << endl;
    }
    return 0;
}
