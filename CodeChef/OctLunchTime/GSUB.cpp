#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<bitset>
#include<algorithm>

using namespace std;

#define fi(i,N) for(int i=0;i<N;i++)
#define fd(N,i) for(int i=N-1;i>=0;i--)
#define ll long long

int NSSQ(int A[],int L){
   int max=1,Fmax=0;
   fi(i,L-1){
      if (A[i]==A[i+1]){
         if (Fmax<max){
            Fmax=max;
            max=1;
         }
         i++;
      }else{
         max++;
         
      }
   }
   // cout<<Fmax<<max<<endl;
   return std::max(Fmax,max);
}

int main(){
   int T,N,Q;
   cin>>T;
   fi(t,T){
      cin>>N>>Q;
      int A[N],B[N];
      fi(i,N){
         cin>>B[i];
      }
      fi(i,Q){
         fi(i,N){
            A[i]=B[i];
         }
         int ind,rpl;
         cin>>ind>>rpl;
         A[ind]=rpl;
         cout<<NSSQ(A,N)<<endl;
      }
   }
}