#include  <iostream>
using namespace std;
#include <vector>

int main(){
          int num,total=0;
          double ave = 0;
          cin >> num;
          vector<int> v(num);

          for (int i = 0; i < num; i++){
                    int a;
                    cin >> a;
                    // cout << a << endl;
                    total += a;
                    v.push_back(a);
                    // この」関数が五かなく、格納されない
          }
          cout << v.at(0) << endl;
          cout << v.at(1) << endl;

          ave = total / num;
          cout << ave << endl;
          for (int i = 0; i < num; i++){
                    cout << v.at(i) << endl;
          }         


}
