#include <iostream>
using namespace std;

int main() {
    int k, p, m, n;
    cin >> k;
    int* b = new int[k];
    for(int c=0;c<k;c++)
    {
        cin >> p >> m;
        int* a = new int[m];
        for (int i = 0; i < m; i++) 
            a[i] = 0;
        int ans = 0;
        for (int i = 0; i < p; i++) 
        {
            cin >> n;
            a[n - 1]++;
        }
        for (int i = 0; i < m; i++) 
        {
            if (a[i] > 1)
                ans += a[i] - 1; 
        }
        b[c] = ans;
    }
    for (int a = 0; a < k; a++)
    {
        cout << b[a]<<endl;
    }
    return 0;
}


