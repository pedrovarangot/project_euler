#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

long sum(long n) {
    return (n*(n+1) >> 1);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int cases;
    
    cin >> cases;
    for(int i = 0; i < cases; ++i) {
        long max;
        cin >> max;
        long max3 = floor((max - 1) / 3);
        //cout << floor(max / 3) << endl;
        long max5 = floor((max - 1) / 5);
        long max15 = floor((max - 1) / 15);
        
        cout << 3*sum(max3) + 5*sum(max5) - 15*sum(max15) << endl;
    }
    return 0;
}
