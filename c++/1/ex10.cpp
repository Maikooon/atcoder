#include <iostream>
using namespace std;

int main()
{
    int a, b, counta = 0, countb = 0;
    cin >> a >> b;
    while (counta < a)
    {
        cout << "]";
        counta++;
    }
    cout << endl;
    while (countb < b)
    {
        cout << "]";
        countb++;
    }
    cout << endl;
}