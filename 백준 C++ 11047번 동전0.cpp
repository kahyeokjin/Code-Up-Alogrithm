#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int lower(int num, int num2)
{
	return num > num2;
}
int main()
{
	int n, k,count=0;
	cin >> n >> k;
	vector <int> coin(n);
	for (int i = 0; i < n; i++)
	{
		cin >> coin[i];
	}
	sort(coin.begin(), coin.end(), lower);
	for (int i = 0; i < n; i++)
	{
		while (k - coin[i] >= 0)
		{
			count++;
			k -= coin[i];
			
		}
	}
	cout << count<<endl;
	return 0;

}