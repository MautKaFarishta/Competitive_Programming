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
   int T;
   cin>>T;
   fi(t,T){
      int N,K,att=0;
      cin >> N >> K;
      char S[N];
      fi(i,N){
         cin>>S[i];
      }
      int magnets= count(S.begin(),S.end(),"M");
      fi(s,N){
         if (S[s]=="M"){
            if ( checkLeft(s)>=0 || checkRight(s)>=0 ){
               att++;
            }
         }
      }
   }
}