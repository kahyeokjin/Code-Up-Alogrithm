#include<iostream>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
	int ksum = 0;
	int wsum = 0;
	vector <int>w(10);
	vector <int>k(10);
	for (int i = 0; i < 10; i++)
	{
		cin >> w[i];
	}
	for (int i = 0; i < 10; i++)
	{
		cin >> k[i];
	}
	sort(w.begin(), w.end());
	sort(k.begin(), k.end());
	for (int i = 7; i < 10; i++)
	{
		wsum += w[i];
	}
	for (int i = 7; i < 10; i++)
	{
		ksum += k[i];
	}
	cout << wsum << " " << ksum << endl;
	return 0;
}