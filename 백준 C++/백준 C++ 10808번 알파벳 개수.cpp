#include <iostream>
#include <string>
using namespace std;

int main()
{
	string s;
	cin >> s;
	int list[26] = { 0, };
	
	for (int i = 0; i < s.size(); i++)
	{
		list[s[i] - 'a']++;
	}
	for (int i = 0; i < 26; i++)
	{
		cout << list[i]<<" ";
	}
	return 0;
}