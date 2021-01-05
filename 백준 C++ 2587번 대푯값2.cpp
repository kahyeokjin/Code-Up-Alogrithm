#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main()
{
	vector <int> num(5);
	int sum = 0;
	for (int i = 0; i < 5; i++)
	{
		cin >> num[i];
		sum += num[i];
	}
	int avg = sum / 5;
	sort(num.begin(), num.end());
	cout << avg << endl;
	cout << num[2];
	return 0;
}