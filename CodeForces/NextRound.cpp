#include<iostream>
#include<bits/stdc++.h>
#include<vector>
#include<bitset>

using namespace std;

#define f(i,N) for(int i=0;i<N;i++)
#define ll long long

int main(){
   int participants,qualifier,minMarks,marks,passed=0;
   cin>>participants>>qualifier;
   int p[participants];
   f(i,participants){
      cin>>p[i];
   }
   minMarks=p[qualifier-1];
   f(i,participants){
      if (p[i]>=minMarks && p[i]>0){
         passed++;
      }
   }
   cout<<passed<<endl;
}