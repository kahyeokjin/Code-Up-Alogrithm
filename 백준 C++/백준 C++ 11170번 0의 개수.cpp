#include <iostream>
using namespace std;

int find(int num)
{
	if (!num)
		return 1;
	int count = 0;
	while (num)
	{
		if (!(num % 10))
		{
			count++;
		}
		num = num / 10;
	}
	return count;
}
int main()
{
	int t;
	cin >> t;
	
	for (int i = 0; i < t; i++)
	{
		int n, m;
		cin >> n >> m;
		int sum = 0;
		for(int a = n; a <= m; a++)
		{
			sum = sum + find(a);
		}
		cout << sum << endl;
	}
}
