#include <iostream>
#include <string>
#include <list>
#include <algorithm>
using namespace std;
int main(int argc, char const *argv[])
{
    list<string> mylist;
    string word;
    cout << "enter your word" << endl;
    cin >> word;
    for (int index = 0; index < word.length(); index++)
    {
        if (word[index] == word[word.length() - 1 - index])
        {
            mylist.push_back("true");
        }
        else
        {
            mylist.push_back("false");
        }
    }
    if (count(mylist.begin(), mylist.end(), "false") == 0)
    {
        cout << "word is a palindrome" << endl;
    }
    else
    {
        cout << "word is not a palindrome" << endl;
    }

    return 0;
}
