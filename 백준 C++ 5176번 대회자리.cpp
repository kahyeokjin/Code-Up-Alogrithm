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
        for (int i = 0; i < m; i++) //제공되는 자리갯수만큼 0으로 지정
            a[i] = 0;
        int ans = 0;
        for (int i = 0; i < p; i++) //참가자들이 원하는 자리에 +1씩
        {
            cin >> n;
            a[n - 1]++;
        }
        for (int i = 0; i < m; i++) //자리수만큼 참여가능,ans는 참가못하는사람의수
        {
            if (a[i] > 1)
                ans += a[i] - 1; //참가할떄 -1
        }
        b[c] = ans;
    }
    for (int a = 0; a < k; a++)
    {
        cout << b[a]<<endl;
    }
    return 0;
}


