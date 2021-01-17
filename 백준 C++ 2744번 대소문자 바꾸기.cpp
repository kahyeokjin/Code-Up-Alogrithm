#include <iostream>
#include <string>
using namespace std;
int main()
{
	string ans;
	cin >> ans;
	for (int i = 0; i < ans.length(); i++)
	{
		char c = ans[i];
		if (('a' <= c) && (c <= 'z'))
		{
			ans[i] = ans[i] - 32;
		}
		else
		{
			ans[i] = ans[i] + 32;
		}
		
	}
	cout << ans << endl;
	return 0;
}
