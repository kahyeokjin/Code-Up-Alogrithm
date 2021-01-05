#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int t;
	cin >> t;
	vector <int> v(t);
	for (int i = 0; i < t; i++)
	{
		cin >> v[i];
	}
	sort(v.begin(), v.end());
	for (int i = 0; i < t; i++)
	{
		cout << v[i] << endl;
	}
	return 0;
}
