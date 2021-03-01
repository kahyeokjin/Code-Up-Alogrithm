#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	int N;
	cin >> N;
	vector<pair<int, int>> ans(N);

	for (int i = 0; i < N; i++)
	{
		cin >> ans[i].first>> ans[i].second;
	}
	sort(ans.begin(), ans.end());

	for (int a = 0; a < N; a++)
	{
		cout << ans[a].second << ' ' << ans[a].first << '\n';
	}
	return 0;

}