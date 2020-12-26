#include <iostream>
using namespace std;

int main()
{
	int list[10],sum=0;
	for (int i = 0; i < 10; i++)
	{
		cin >> list[i];
		sum = sum + list[i];
	}
	double average = sum / 10;
	
	int list2[10], num1,list3[10],count=0,big=0,index;
	
	for (int j = 0; j < 10; j++)
	{
		for (int k = 0; k < 10; k++)
		{
			num1 = list[j];
			list2[j] = list[j];
			if (list[k] == num1)
			{
				count++;
			}
		}
		list3[j] = count;
		count = 0;
	}
	for (int i = 0; i < 10; i++)
	{
		if (list3[i] > big)
		{
			big = list3[i];
			index = list[i];
		}
	}
	cout << average << '\n' << index;
	return 0;
}