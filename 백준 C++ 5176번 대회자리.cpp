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
        for (int i = 0; i < m; i++) //�����Ǵ� �ڸ�������ŭ 0���� ����
            a[i] = 0;
        int ans = 0;
        for (int i = 0; i < p; i++) //�����ڵ��� ���ϴ� �ڸ��� +1��
        {
            cin >> n;
            a[n - 1]++;
        }
        for (int i = 0; i < m; i++) //�ڸ�����ŭ ��������,ans�� �������ϴ»���Ǽ�
        {
            if (a[i] > 1)
                ans += a[i] - 1; //�����ҋ� -1
        }
        b[c] = ans;
    }
    for (int a = 0; a < k; a++)
    {
        cout << b[a]<<endl;
    }
    return 0;
}


