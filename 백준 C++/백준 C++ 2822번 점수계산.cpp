#include <iostream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

int main()
{
	vector<pair<int, int>>score(8);
	
	for (int i = 0; i < 8; i++)
	{
		cin >> score[i].first;
		score[i].second = i + 1;
	}
	sort(score.begin(), score.end(), greater<pair<int, int>>());
	
	vector<int>que;
	int sum = 0;
	for (int i = 0; i < 5; i++)
	{
		sum = sum + score[i].first;
		que.push_back(score[i].second);
	}
	cout << sum<<'\n';

	sort(que.begin(), que.end());
	for (int i = 0; i < que.size(); i++)
	{
		cout << que[i]<<' ';
	}
	
	return 0;
}
