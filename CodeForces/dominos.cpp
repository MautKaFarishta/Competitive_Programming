#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<bitset>

using namespace std;

#define f(i,N) for(int i=0;i<N;i++)
#define ll long long

int main(){
   int M,N;
   cin>>M>>N;
   if(M<2 && N<2){
      cout<<"0";
   }else{
      int area=M*N;
      cout<<floor(area/2)<<endl;
   }
}