#include <iostream>
using namespace std;

int main()
{
    int n, a, ans;
    cin >> n >> a;
    ans = a;
    for (int i = 0; i < n; i++)
    {
        string s;
        int b;
        cin >> s >> b;
        if (s == "+")
        {
            ans += b;
        }
        else if (s == "-")
        {
            ans -= b;
        }
        else if (s == "*")
        {
            ans *= b;
        }
        else if (s == "/")
        {
            ans /= b;
        }
        cout << i+1 << ":" << ans << endl;
    }
    return  0;
}