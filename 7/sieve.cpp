#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

static const int MAX = 1000;
vector<bool> isprime(MAX);

int main()
{
    int n;

    for(int i = 0; i < MAX; ++i) isprime[i] = true;
    isprime[0] = false;
    isprime[1] = false;
    
    cin >> n;

    for(int i = 2; i < (int)sqrt(MAX); ++i) {
        if(isprime[i]) {
            for(int j = 2; j < (int)sqrt(MAX); ++j) {
                isprime[j*i] = false;
            }
        }
    }
   
    int counter = 0;
    for(auto i:isprime) {
        if(i) n--;
        if(n == 0) break;
        counter++;
    }
    cout << counter << endl;  

    return 0;
}
