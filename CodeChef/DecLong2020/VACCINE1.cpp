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
   int D,V,d,v;
   int P=14,currV=0,day=0;
   cin>>D;
   cout<<"Input1";
   cin>>V;
   cout<<"Input2";
   cin>>d;
   cout<<"Input3";
   cin>>v;
   cout<<"Input4";
   // cin>>P;
   cout<<"Input5";
   while(currV<P){
      if(day>=D){
         currV=currV+V;
      }if(day>=d){
         currV=currV+v;
      }
   }
   cout<<day<<endl;
}