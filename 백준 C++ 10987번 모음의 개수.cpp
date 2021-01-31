#include <iostream>
#include <string>

using namespace std;

int main()
{
	string word;
	cin >> word;
	int length = word.length();
	int count = 0;
	for (int i = 0; i < length; i++)
	{
		if (word[i] == 'a')
			count++;
	}
	for (int i = 0; i < length; i++)
	{
		if (word[i] == 'e')
			count++;
	}
	for (int i = 0; i < length; i++)
	{
		if (word[i] == 'i')
			count++;
	}
	for (int i = 0; i < length; i++)
	{
		if (word[i] == 'o')
			count++;
	}
	for (int i = 0; i < length; i++)
	{
		if (word[i] == 'u')
			count++;
	}
	cout << count << endl;
	return 0;
}