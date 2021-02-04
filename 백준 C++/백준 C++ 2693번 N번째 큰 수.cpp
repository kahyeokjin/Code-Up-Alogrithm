#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	int t,list[10];
	cin >> t;
	int* result = new int[t];
	for(int a=0;a<t;a++)
	{
		for (int i = 0; i < 10; i++)
		{
			cin >> list[i];
		}
		sort(list, list + 10);
		result[a] = list[7];
	}
	for (int a = 0; a < t; a++)
	{
		cout << result[a] << endl;
	}
	result;
}
