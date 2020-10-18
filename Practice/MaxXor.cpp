#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main(){
   int n;
   cin>>n;
   int arr[n];
   for (int i=0;i<n;i++) cin>>arr[i];
   int qury;
   cin>>qury;
   while (qury--){
      int x,maxXOR=0;
      cin>>x;
      for (int j=0 ; j<n;j++){
         if (maxXOR<(x^arr[j])){
            maxXOR=(x^arr[j]);
         }
      }
      cout<<maxXOR;
   }
}