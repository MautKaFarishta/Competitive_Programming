#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<bitset>
#include<algorithm>

using namespace std;

#define fi(i,N) for(int i=0;i<N;i++)
#define fd(N,i) for(int i=N-1;i>=0;i--)
#define ll long long

void primeInRange(int N,int *primes) 
{ 
   int num=1,primeCount=0,Pgot=0;
   while(Pgot<N){
      num++;//num = 2
      primeCount = 0;
      for(int i = 1; i <= num; i++){
         if(num % i == 0){
            primeCount++;
        }
      }
      if(primeCount == 2){
            primes[Pgot]=num;
            Pgot++;
      }
   }
} 


int main(){
   int L=2,H=4000000,T,N,tempIndex;
   cin>>T;
   fi(t,T){
      cin>>N;
      int A[N],B[N],primes[N];
      primeInRange(N,primes);
      fi(n,N){
         cin>>B[n];
      }
      fi(i,N){
         if (i+1==B[i]){
            A[i]=primes[i];
         }else{
            A[i]=primes[B[i]-1];
         }
      }
      fi(i,N){
         cout<<A[i]<<" ";
      }cout<<endl;
   }
}
