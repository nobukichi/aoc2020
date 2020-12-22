#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <utility>

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

  int n;
  cin >> n;
  deque<int> q[2];
  rep(p, 2) {
    rep(i, n) {
      int v;
      cin >> v;
      q[p].push_back(v);
    }
  }
  int round = 1;
  while (!q[0].empty() && !q[1].empty()) {
    int v[2];
    rep(p, 2) {
      v[p] = q[p].front();
      q[p].pop_front();
    }
    rep(p, 2) {
      if (v[1-p] < v[p]) {
        q[p].push_back(v[p]);
        q[p].push_back(v[1-p]);
        cerr << "round " << round << ", winner is player " << p << ", remaining cards: " << q[0].size() << ' ' << q[1].size() << endl;
      }
    }
    ++round;
  }
  int winner = q[0].empty() ? 1 : 0;
  cerr << "Final winner = " << winner << endl;
  int ans = 0;
  for (int f = q[winner].size(); 1 <= f; --f) {
    ans += f * q[winner].front();
    q[winner].pop_front();
  }
  cout << "ans: " << ans << endl;

  return 0;
}

