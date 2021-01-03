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
   int t;
   cin>>t;
   fi(i,t){
      int N;
      cin>>N;
      int dishes[N];
      fi(j,N){
         cin>>dishes[j];
      }
      int n = sizeof(dishes) / sizeof(dishes[0]); 
      sort(dishes, dishes+n); 
      int X=0,Y=0;
      fd(N,k){
         if (k==N-1){
            X=X+dishes[k];
         }else{
         if(X<Y){
            X=X+dishes[k];
         }else{
            Y=Y+dishes[k];
         }}
      }
      cout << std::max(X,Y) << endl;
   }
}