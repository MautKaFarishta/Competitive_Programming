#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<bitset>
#include<algorithm>

using namespace std;

#define fi(i,N) for(int i=0;i<N;i++)
#define fd(N,i) for(int i=N-1;i>=0;i--)
#define ll long long

int main(){
   int T;
   cin>>T;
   fi(i,T){
      ll num;
      cin>>num;
      if(num%2==1){
         cout<<num/2<<" "<<num/2+1<<endl;
      }else{
         cout<<num/2<<" "<<num/2<<endl;
      }
   }
}