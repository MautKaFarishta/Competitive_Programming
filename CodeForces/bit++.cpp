#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<bitset>

using namespace std;

#define f(i,N) for(int i=0;i<N;i++)
#define ll long long

int main(){
   int opr,val=0;
   cin>>opr;
   f(i,opr){
      string cp;
      cin>>cp;
      if(cp.find('+')<cp.length()){ 
         val++;
         // cout<<val;
      } else {
         val--;
         // cout<<val;
      }
   }
   cout<<val;
}