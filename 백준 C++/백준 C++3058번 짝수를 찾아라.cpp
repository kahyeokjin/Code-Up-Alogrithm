#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int t=0;
	cin >> t;
	vector <int> v(7);
	vector <pair<int, int>> result(t);
	for (int i = 0; i < t; i++)
	{
		int sum = 0;
		int num = 0;
		v.assign(7, 0);
		for (int a = 0; a < 7; a++)
		{
			cin >> v[a];
			if (v[a] % 2 != 0)
			{
				v[a] = 0;
			}
			sum += v[a];
		}
		sort(v.begin(), v.end());
		for (int j = 0; ;j++)
		{
			if (v[j] != 0)
			{
				num = j;
				break;
			}
		}
		result[i].first = sum;
		result[i].second = v[num];
		
	}
	for (int i = 0; i < t; i++)
	{
		cout << result[i].first << " " << result[i].second << endl;
	}
	return 0;
}
