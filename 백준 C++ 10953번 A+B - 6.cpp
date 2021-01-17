#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int t;
	cin >> t;
	vector <int> ans(t);
	for (int a=0; a < t; a++)
	{
		int aa, b;
		char c;
		cin >> aa >> c >> b;
		ans[a] = aa + b;
	}
	for (int a=0; a < t; a++)
	{
		cout << ans[a] << endl;
	}
	return 0;
}