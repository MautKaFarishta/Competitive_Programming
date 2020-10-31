#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<bitset>
#include<algorithm>

using namespace std;

#define f(i,N) for(int i=0;i<N;i++)
#define ll long long

int main(){
   string su,tu;
   cin>>su>>tu;
   transform(su.begin(), su.end(), su.begin(), ::toupper);
   transform(tu.begin(), tu.end(), tu.begin(), ::toupper);
   if(su<tu){
      cout<<"-1"<<endl;
   }else if(su>tu){
      cout<<"1"<<endl;
   }else{
      cout<<"0"<<endl;
   }
}
