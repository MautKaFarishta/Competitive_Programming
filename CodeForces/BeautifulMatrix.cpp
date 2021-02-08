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
   int row=0,col=0,test,f=0;
   fi(i,5){
      col=0;row++;
      fi(j,5){
         col++;
         cin>>test;
         if(test==1){
            f=1;
            break;
         }
      }
      if(f==1){
         break;
      }
   }
   cout<<abs(col-3)+abs(row-3)<<endl;
}