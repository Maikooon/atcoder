#include <iostream>
using namespace std;
int main()
{
    int type;
    double x;
    cin >> type;
    if (type == 1)
    {
        int a, b;
        cin >> a >> b;
        x = a * b;
    }
    else if (type == 2)
    {
        int a, b;
        string s;
        cin >> s >> a >> b;
        x = a * b;
        cout << s << "!" << endl;
    }

    cout << x << endl;
    return 0;
}
