#include <iostream>
using namespace std;

int main()
{
    int x, a, b;
    cin >> x >> a >> b;
    int ans;
    ans = x + 1;
    cout << ans << endl;
    ans *= a + b;
    cout << ans << endl;
    ans *= ans;
    cout << ans << endl;
    ans -= 1;
    cout << ans << endl;
}