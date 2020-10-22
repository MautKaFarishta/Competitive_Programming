#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll SubArraySum( vector<ll> arr , ll n ) 
{ 
    ll result = 0,i; 
  
    for (i=0; i<n; i++) 
    {
        result += (arr[i] * (i+1) * (n-i));
    cout<<arr[i]<<" "; 
    }
    return result ; 
} 
ll hBit(ll n) 
{ 
   
   if (n == 0) 
        return 0; 
  
    int msb = 0; 
    n = n / 2; 
    while (n != 0) { 
        n = n / 2; 
        msb++; 
    } 
  
    return (1 << msb); 
} 
ll calc(ll a[],ll n)
{
  ll x=a[0],i;
  for(i=1;i<n;i++){
    x=(x^a[i]);
    x=hBit(x);
  }
  return x;
}
ll solve(ll a[],ll n,ll s) 
{
  ll i,m=10000000000;
  if(s==1) {
    return calc(a,n);
  }
  for(i=0;i<s;i++) 
  {
    m=min(m,solve(a,n,s-1));
    if(n%2!=0)
      swap(a[i],a[s-1]);
    else
      swap(a[0],a[s-1]);
  }
  return m;
}
int main()
{
  ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
  ll n;
  cin>>n;
  ll i,j,x,s=0,l,m,k,p,r;
  ll a[n];
  vector<ll> v;
  for(i=0;i<n;i++)
  {
    cin>>a[i];
    s=s+a[i];
    s=s%998244353;
  }
  for(i=0;i<(n-1);i++)
  {
    x=(a[i]^a[i+1]);
    s=s+hBit(x);
    s=s%998244353;
  }
  for(l=0;l<n;l++)
  {
    for(r=l+2;r<n;r++){
      ll b[r-l+1];
      i=0;
      for(k=l;k<=r;k++){
        b[i]=a[k];
        i++;
      }
      x=solve(b,r-l+1,r-l+1);
      s=s+x;
      s=s%998244353;  
    }
  }
  cout<<s%998244353;
  //cout<< SubArraySum(v, v.size()); 
  return 0;
}