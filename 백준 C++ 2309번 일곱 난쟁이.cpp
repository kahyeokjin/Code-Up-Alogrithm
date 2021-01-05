#include <iostream>
#include <algorithm>

using namespace std;

int sol(int sum, int* li)
{
	for (int a = 0; a < 8; a++)
	{
		for (int b = 1; b < 9; b++)
		{
			if (sum - (li[a] + li[b]) == 100)
			{
				li[a] = -1;
				li[b] = -1;
				return 0;
			}
		}
	}
}

int main()
{
	int sma[9],sum=0;
	for (int i = 0; i < 9; i++)
	{
		cin >> sma[i];
		sum += sma[i];
	}
	sol(sum, sma);
	sort(sma, sma+9);
	for (int i = 2; i < 9; i++)
	{
		cout << sma[i]<<endl;
	}
	return 0;



}