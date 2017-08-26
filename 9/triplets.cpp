#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    int t;
    cin >> t;
    vector<int> triplet_product_N(3001*3);
    for(int i = 0; i < 3001*3; ++i) triplet_product_N[i] = -1;
    long int N = -1;
    for(int c = 1; c <= 3000; ++c) {
        //cout << "c: " << c << endl;
        for(int b = 1; b < c && b + c <= 3000; ++b) {
            //cout << "b: " << b << endl;
            for(int a = 1; a < b && a + b + c <= 3000; ++a) {
                //cout << "a: " << a << endl;
                if(a*a + b*b == c*c && a*b*c > triplet_product_N[a+b+c]) {
                    triplet_product_N[a+b+c] = a*b*c;
                    //cout << a << " " << b << " " << c << endl
                }
            }
        }
    }
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;

        cout << triplet_product_N[n] << endl;
    }
    return 0;
}
