#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

static const int MAX = 50000;
vector<int> triangles_divisors(MAX);

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int t;
    cin >> t;
    
    for(int i = 0; i < MAX; ++i) {
        int triangle_number = i*(i+1)/2;
        int divisors = 1;
        //cout << i << " triangle number that is " << i*(i+1)/2 << endl;
        for(int j = 2; j <= sqrt(triangle_number); ++j) {
            int factor_n = 0;
            while(triangle_number % j == 0) {
                //cout << "factor! " << j << endl;
                triangle_number /= j;
                //cout << triangle_number << endl;
                factor_n++;
            }
            divisors *= factor_n + 1; 
        }
        if(triangle_number > 1) {
            //cout << "factor! " << triangle_number << endl;
            divisors *= 2;
        }
        //cout << divisors << " divisors" << endl;
        triangles_divisors[i] = divisors;
    }
    triangles_divisors[1] = 1; 
    
    int tot = 0;
    for(int a0 = 0; a0 < t; ++a0) {
        int n;
        cin >> n;
        for(int i = 1; i < MAX; ++i) {
            if(triangles_divisors[i] > n) {
                cout << i*(i+1)/2 << " " << i << endl;
                tot++; 
                break;
            }
        }
    }
    //cout << tot << " " << t << endl;
    return 0;
}

