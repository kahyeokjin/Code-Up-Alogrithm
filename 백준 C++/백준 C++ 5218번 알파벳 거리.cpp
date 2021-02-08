#include <iostream>
#include <string>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int a = 0; a < t; a++)
	{
		string s1,s2;
		cin >> s1 >> s2;
		cout << "Distances: ";
		for (int i = 0; i < s1.size(); i++)
		{
			if ((int)s1[i] > (int)s2[i])
			{
				cout << s2[i] - s1[i] + 26 << " ";
			}
			else
			{
				cout << s2[i] - s1[i] << " ";
			}
		}
		cout << endl;
	}
	return 0;
	
}