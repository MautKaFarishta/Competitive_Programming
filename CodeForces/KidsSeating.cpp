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
   int T,N,d=4;
   cin>>T;
   fi(i,T){
      d=4;
      cin>>N;
      if (N==1){
         cout<<"1"<<endl;
      }else{
         fi(i,N){
            if(i==N-1){
               if(d%4==0){
                  d=d+2;
               }
            }
            cout<<d<<" ";
            d=d+2;
         }
         cout<<endl;
      }
   }
}