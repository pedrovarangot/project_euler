#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

bool isprime(int n)
{
    if(n < 0) return false;
    if(n == 2) return true;
    if(n == 3) return true;
    if(n == 5) return true;
    
    for(int k = 2; k < sqrt(n) + 1; ++k) {
        if(n % k == 0) return false;
    }
    return true;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    cin >> n;
    
    int res;
    int max = 0, founda, foundb;
    for(int a = -n; a <= n; ++a) {
        for(int b = -n; b <= n; ++b) {
            int k;
            for(k = 0; k <= n && isprime(k*k + a*k + b); ++k) {
                //cout << k*k + a*k + b << " " << isprime(k*k + a*k + b) << endl;
                //cout << "loop: " << k << endl;
            }
            if(k > max) {
                max = k;
                founda = a;
                foundb = b;
            }

        }
    }
    cout << founda << " " << foundb << endl;
    
    return 0;
}
