#include <iostream>
using namespace std;

int main()
{
	int num1;
	cin >> num1;


	char c;
	int sum = 0;
	for (int i = 0; i < num1; i++)
	{
		cin >> c;
		sum = sum + (c - '0');
	}

	cout << sum;
	return 0;


}