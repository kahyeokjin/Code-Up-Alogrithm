#include <iostream>
#include <string>
using namespace std;
int main()
{
	string n;
	int m;
	cin >> n >> m;
	int num = stoi(n);
	int length = n.length();
	string result;

	if (num * length >= m)
	{
		int a = 0;
		while (1)
		{
			if (a + length > m)
			{
				break;
			}
			result += n;
			a += length;
		}
		for (int i = 0; i < m - a; i++)
		{
			result += n[i];
		}
	}
	else
	{
		for (int i = 0; i < num; i++)
		{
			result = result + n;
		}
	}
	cout << result << endl;
	return 0;
}
