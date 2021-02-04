#include <iostream>
#include <string>

using namespace std;

int main()
{
	string word;
	getline(cin, word);
	
	for (int i = 0; i < word.size(); i++)
	{
		cout << word[i];
		if ((i+1) % 10 == 0)
		{
			cout << '\n';
		}
	}
	return 0;
}