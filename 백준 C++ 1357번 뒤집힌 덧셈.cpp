#include <iostream>
using namespace std;

int change(int num)
{
	int n=0;
	while (num > 0)
	{
		n = n * 10;
		n = n + num % 10;
		num = num / 10;
	}
	return n;
}
int main()
{
	int x, y;
	cin >> x >> y;
	cout << change(change(x) + change(y));
	return 0;
}