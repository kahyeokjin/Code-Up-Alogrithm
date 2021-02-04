#include <iostream>
#include <string>
using namespace std;

int main()
{
	int num1, num2, num3;
	int list[10] = { 0 };
	cin >> num1 >> num2 >> num3;
	int num = num1 * num2 * num3;

	while (num != 0)
	{
		list[num % 10] += 1;
		num = num / 10;
	}
	for (int i = 0; i < 10; i++)
	{
		cout << list[i] << endl;
	}
	return 0;
}
