#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s;
	int alp[26] = { 0, };

	cin >> s;

	for (int i = 0; i < s.length(); i++)
	{
		int n = s[i];
		if (n < 97)
			alp[n - 65]++;
		else
			alp[n - 97]++;
	}
	int max = 0;
	int index = 0;
	for (int i = 0; i < 26; i++)
	{
		if (alp[i] > max) {
			max = alp[i];
			index = i;
		}
	}
	int count = 0;
	for (int i = 0; i < 26; i++)
	{
		if (alp[i] == max)
		{
			count++;
			if (count >= 2) {
				cout << "?" << endl;
				return 0;
			}
		}
	}
	cout << char(index + 65) << endl;
	return 0;
}