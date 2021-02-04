#include <iostream>
#include <string>

using namespace std;

int main()
{
	string memo;
	
	cin >> memo;
	cout << memo[0];
	for (int i = 1; i < memo.size(); i++)
	{
		if (memo[i] != '-')
		{
			continue;
		}
		else if (memo[i] == '-' && i + 1 < memo.size())
		{
			cout << memo[i+1];
		}
	}
	
	return 0;
}
