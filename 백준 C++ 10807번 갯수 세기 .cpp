#include <iostream>
using namespace std;
int main()
{
	int N, list[100] = { 0 }, num, count = 0;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> list[i];
	}
	cin >> num;
	for (int i = 0; i < N; i++)
	{
		if (list[i] == num)
			count++;
	}
	cout << count;
	return 0;
}