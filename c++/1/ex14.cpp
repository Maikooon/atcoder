#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
          // vector<int> sort(3);
          int a,b,c;
          int diff ;

          // 全ての入力を配列に入れたい
          cin >> a >> b >> c;
          vector<int> sorted = {a,b,c};
          sort(sorted.begin(),sorted.end());     
          diff = sorted.at(2) - sorted.at(0);             
          cout << diff << endl;
}