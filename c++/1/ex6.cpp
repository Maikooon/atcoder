#include <iostream>
using namespace std;

int main()
{
    int a, b;
    string s;

    cin >> a >> s >> b;
    if (s == "+")
    {
        cout << a + b << endl;
    }
    else if (s == "-")
    {
        cout << a - b << endl;
    }
    else if (s == "*")
    {
        cout << a * b << endl;
    }
    else if (s == "/")
    {
        if (b == 0)
        {
            cout << "error" << endl;
        }
        else
        {
            cout << a / b << endl;
        }
    }
    else if (s == "?" or s == "=" or s == "!")
    {
        cout << "error" << endl;
    }
}