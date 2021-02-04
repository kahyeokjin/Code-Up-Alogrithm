#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	int k = 0;
	cin >> k;
	vector <pair<int, int>> ans(k);
	vector <int> ans2(k);
	for (int i = 0; i < k; i++)
	{
		int max = 0, low = 100, gap = 0;
		int stu;
		cin >> stu;
		vector <int> cla(stu); 
		for (int a = 0; a < cla.size(); a++)
		{
			cin >> cla[a];
			if (max < cla[a])
				max = cla[a];
			if (low > cla[a])
				low = cla[a];
		}
		sort(cla.begin(), cla.end());
		for (int b = 1; b < stu; b++)
		{
			if (gap < cla[b] - cla[b - 1])
				gap = cla[b] - cla[b - 1];
		}
		ans[i].first = max;
		ans[i].second = low;
		ans2[i] = gap;
		
	}
	for (int i = 0; i < k; i++)
	{
		cout << "Class " << i+1 << endl;
		cout << "Max " << ans[i].first << ", Min " << ans[i].second << ", Largest gap " << ans2[i] << endl;
	}
	return 0;
}
