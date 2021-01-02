#include <iostream>
using namespace std;
int main()
{
	int list[1000],num=1,p=0,a,b,sum=0;
	cin >> a >> b;
	for (int i = 0; p < 1000; i++)
	{
		for (int j = 0; j <= i; j++)
		{
			list[p++] = num;
			if (p == 1000)
				break;
		}
		num++;
	}
	for (int k = a-1; k <= b-1; k++)
	{
		sum = sum + list[k];
	}
	cout << sum;
	
	return 0;
}

