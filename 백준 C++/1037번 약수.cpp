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
	int result = v[0] * v[t - 1];
	cout << result;
	return 0;
}
