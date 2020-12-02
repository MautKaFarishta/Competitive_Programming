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
   int N;
   cin>>N;
   int A[N][N];
   fi(i,N){
      fi(j,N){
         cin>>A[i][j];
      }
   }
   int track,flag=0;
   fi(i,N-1){
      track=0;
      for(int j=i+1;j<N;j++){
         if(A[i][j]==1){
            track++;
         }
      }
      if (track%2==0){
         cout<<"1"<<endl;
         flag=1;
         break;
      }
   }
   if (flag==0){
      cout<<"0"<<endl;
   }
}