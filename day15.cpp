#include <iostream>
#include <algorithm>
#include <vector>
#include <map>

using namespace std;

typedef long long LL;

#define rep(i,n) for (int i = 0; i < int(n); ++i)
#define repr(i,from,to) for (int i = int(from); i <= int(to); ++i)

template<class T>bool chmax(T &a, const T &b) { if (a<b) { a=b; return true; } return false; }
template<class T>bool chmin(T &a, const T &b) { if (b<a) { a=b; return true; } return false; }

#define dump(c) { for (auto it = c.begin(); it != c.end(); ++it) if (it == c.begin()) cout << *it; else cout << ' ' << *it; cout << endl; }
#define dumpMap(m) { for (auto it: m) cout << it.first << "=>" << it.second << ' '; }

typedef pair<int, int> P;
#define F first
#define S second

const int INF = 1e9;
const LL INFL = 1e18;
const int MOD = 1000000007;


int main()
{
  cin.tie(0);
  ios::sync_with_stdio(0);

  // const int YEAR = 2020;
  const int YEAR = 30000000;

  vector<int> a = { -1, 0,12,6,13,20,1,17 };
  // vector<int> a = { -1, 0,3,6 };

  int n = a.size()-1;
  map<int, vector<int>> past;
  repr(i, 1, n) {
    past[a[i]].push_back(i);
  }
  repr(i, n+1, YEAR) {
    int pre = a[i-1];
    int num = 0;
    int occ = past[pre].size();
    if (1 < occ) {
      num = past[pre][occ-1] - past[pre][occ-2];
    }
    a.push_back(num);
    if (past[num].size() == 2) {
      past[num][0] = past[num][1];
      past[num][1] = i;
    } else {
      past[num].push_back(i);
    }
  }
  // dump(a);
  cout << "answer = " << a[YEAR] << endl;

  return 0;
}
