#include <iostream>
#include <vector>
using namespace std;
int main()
{
	vector <int>list (9);
	int sum = 0;
	for (int i = 0; i < 9; i++)
	{
		cin >> list[i];
		sum += list[i];
	}
	for (int i = 0; i < 9; i++)
	{
		for (int j = i + 1; j < 9; j++)
		{
			if (sum - list[i] - list[j] == 100)
			{
				for (int k = 0; k < 9; k++)
				{
					if ((k != i) && (k != j))
						cout << list[k] << endl;
				}
				break;
			}
		}
	}
	return 0;
	
}
