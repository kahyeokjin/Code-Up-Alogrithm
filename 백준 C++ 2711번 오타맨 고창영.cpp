#include <iostream>
#include <string>
using namespace std;


int main()
{
	int num, error;
	string str;
	cin >> num;
	for (int i = 0; i < num; i++)
	{
		cin >> error >> str;
		for (int j = 0; j < str.size(); j++)
		{
			if (j != (error - 1))
				cout << str[j];
		}
		cout << '\n';
	}
	return 0;
}