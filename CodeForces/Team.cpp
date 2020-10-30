#include<iostream>

using namespace std;

int main(){
   int N,cnt=0,a,b,c;
   cin>>N;
   for (int i=0;i<N;i++){
      cin>>a>>b>>c;
      if (a+b+c>=2){
         cnt++;
      }
   }
   cout<<cnt<<endl;
}