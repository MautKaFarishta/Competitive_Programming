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
   int N,ans=0;
   cin>>N;
   int A[N];
   fi(i,N){
      cin>>A[i];
   }
   fi(i,N-1){
      ans=ans+abs(A[i]-A[i+1]);
   }cout<<ans<<endl;
}