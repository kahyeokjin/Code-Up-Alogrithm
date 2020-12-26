#include <iostream>
#include <string>
using namespace std;
int main(void)
{
	string num1, num2,answer;
	cin >> num1 >> num2;

	for (int i = 2; i >= 0; --i)
	{
		if (num1[i] > num2[i])
		{
			answer = num1;
			break;
		}
		else if (num1[i] < num2[i])
		{
			answer = num2;
			break;
		}
		else 
			continue;
	}
	cout << answer[2] << answer[1] << answer[0];
	
	return 0;
}