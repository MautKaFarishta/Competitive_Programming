#include<bits/stdc++.h>

using namespace std;

#define ll long long
bool compa(const pair<ll, pair<ll, ll>> &a,
           const pair<ll, pair<ll, ll>> &b)
{
 return a.first > b.first;
}
ll pts[200005][7] = {0};
ll unionset[200002];
ll mnht(ll kth, ll idx, ll d)
{
 ll dist = 0;

 for (ll i = 0; i < d; i++)
 {
  dist += abs(pts[kth][i] - pts[idx][i]);
 }

 return dist;
}
ll findpar(ll ch)
{
 if (unionset[ch] == -1)return ch;
 return unionset[ch] = findpar(unionset[ch]);
}
ll max_cmb(ll cmbn[6],  ll n, ll d)
{
 ll pk = -19372273028659; ll idx = 0;

 for (ll i = 0; i < n; i++)
 {
  ll val = 0;

  for (ll j = 0; j < d; j++)
  {
   val += (1 - 2 * cmbn[j]) * pts[i][j];
  }

  if (val > pk)
  {
   pk = val;
   idx = i;
  }
 }

 return idx;
}

int main()
{
ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
 ll n, d;
 cin >> n >> d;

 for (ll i = 0; i < n; i++)
 {
  for (ll j = 0; j < d; j++)
   cin >> pts[i][j];
 }

 ll pk[2 << d];

 for (ll j = 0; j < 1 << (d); j++)
 {
  ll cmbn[6] = {0};
  for (ll dig = 0; dig < d; dig++)
  {
   if (j & 1 << dig)
    cmbn[dig] = 1;
   // cout<<cmbn[dig]<<" ";
  }
//cout<<endl;
  pk[j] = max_cmb(cmbn, n, d);
 }
 vector <pair<ll, pair<ll, ll>>> graph;
 ll maxd = 0;
 for (ll i = 0; i < n; i++)
 {
  for (ll j = 0; j < 1 << (d); j++)
  {
   ll x = mnht(i, pk[j], d);
   graph.push_back({x, {i, pk[j]}});
  }
 }
 ll tw = 0;
 sort(graph.begin(), graph.end(), compa);
 memset(unionset, -1, sizeof(unionset));
 //cout<<graph.size()<<endl;
 for (ll i = 0; i<graph.size(); i++)
 {
     //cout<<graph[0].second.first<<" "<<graph[0].second.second<<endl;
  ll s1 = findpar(graph[i].second.first);
  ll s2 = findpar(graph[i].second.second);
  if (s1 != s2)
  {
   tw += graph[i].first;
   unionset[s1] = s2;
  }
 }
 cout << tw << endl;
 //cout<<"d";
 return 0;
}
// // C++ program to find a pair with the given difference 
// #include <bits/stdc++.h> 
// using namespace std; 

// // The function assumes that the array is sorted 
// bool findPair(int arr[], int size, int n) 
// { 
// 	// Initialize positions of two elements 
// 	int i = 0; 
// 	int j = 1; 

// 	// Search for a pair 
// 	while (i < size && j < size) 
// 	{ 
// 		if (i != j && arr[j] - arr[i] == n) 
// 		{ 
// 			cout << "Pair Found: (" << arr[i] << 
// 						", " << arr[j] << ")"; 
// 			return true; 
// 		} 
// 		else if (arr[j]-arr[i] < n) 
// 			j++; 
// 		else
// 			i++; 
// 	} 

// 	cout << "No such pair"; 
// 	return false; 
// } 

// // Driver program to test above function 
// int main() 
// { 
// 	int arr[] = {1, 8, 30, 40, 100}; 
// 	int size = sizeof(arr)/sizeof(arr[0]); 
// 	int n = 60; 
// 	findPair(arr, size, n); 
// 	return 0; 
// } 
// C++ program to find a pair with the given difference 
// #include <bits/stdc++.h> 
// using namespace std; 

// // The function assumes that the array is sorted 
// bool findPair(int arr[], int size, int n) 
// { 
// 	// Initialize positions of two elements 
// 	int i = 0; 
// 	int j = 1; 

// 	// Search for a pair 
// 	while (i < size && j < size) 
// 	{ 
// 		if (i != j && arr[j] - arr[i] == n) 
// 		{ 
// 			cout << "Pair Found: (" << arr[i] << 
// 						", " << arr[j] << ")"; 
// 			return true; 
// 		} 
// 		else if (arr[j]-arr[i] < n) 
// 			j++; 
// 		else
// 			i++; 
// 	} 

// 	cout << "No such pair"; 
// 	return false; 
// } 

// // Driver program to test above function 
// int main() 
// { 
// 	int arr[] = {1, 8, 30, 40, 100}; 
// 	int size = sizeof(arr)/sizeof(arr[0]); 
// 	int n = 60; 
// 	findPair(arr, size, n); 
// 	return 0; 
// } 





