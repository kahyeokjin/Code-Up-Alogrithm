#include <iostream>
using namespace std;

int main()
{
	int rest[42] = {0}, num, count=0;

	for (int i = 0; i < 10; i++)
	{
		cin >> num;
		rest[num % 42] = 1;
	}
	
	for (int i = 0; i < 42; i++)
	{
		if (rest[i] == 1)
			++count;
	}
	cout << count;
	return 0;
}