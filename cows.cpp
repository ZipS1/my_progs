#include <iostream>
#include<vector>
#include<cmath>
#include<bits/stdc++.h>

using namespace std;

int n, k;
vector<int> arr;

bool check(int x)
{
    int cows = 1;
    int last_cow = arr[0];
    for(auto i : arr)
    {
        if(i - last_cow >= x)
        {
            cows++;
            last_cow  = i;
        }
    }
    return cows >= k;
}

int ans()
{
    int l = 0, r = arr[n - 1] - arr[0] + 1;
    while(r != l + 1)
    {
        int mid = (l + r) / 2;
        if(check(mid))
        {
            l = mid;
        }
        else
        {
            r = mid;
        }
    }
    return l;
}

int main()
{
    cin >> n >> k;
    arr.resize(n);
    for(int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
    sort(arr.begin(), arr.end());
    cout << ans();


}
