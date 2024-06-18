#include <iostream>
#include <vector>
using namespace std;

int main(){
          string s;
          int count= 0 ;
          cin >> s;
          for (int i =0; i < s.size(); i++){
                    if (i % 2 == 0){
                              count +=1 ;
                    }
                    else{
                              if (s.at(i) == '-'){
                                        count -=2;
                              }
                            

                    }
                    // cout << count << endl;
          }
          cout << count << endl;        
          // 偶奇で分割してm入力を行うll}
}


