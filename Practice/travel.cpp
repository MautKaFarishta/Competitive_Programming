#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<bitset>

using namespace std;

#define f(i,N) for(int i=0;i<N;i++)
#define ll long long

int main(){
   int a[5]={0,0,0,0,0},rank;
   const char *city[5] = { "Malaysia", "Australia", "Germany", "Dubai","France " }; 
   f(i,5){
      f(j,5){
         cin>>rank;
         if (0<rank<6){
            a[j]=a[j]+(5-rank);
         }else{
            cout<<"INVALID INPUT";
         }
      }
   }
   int max=0;
   f(i,5){
      if (max<a[i]){
         max=a[i];
      }
   }
   f(i,5){
      if (a[i]==max){
         cout<<city[i];
      }
   }
}