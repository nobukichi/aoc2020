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


inline LL hashQ(const deque<int>& q) {
  LL ret = 0;
  rep(i, q.size()) {
    ret = (ret * 50 + q[i]) % MOD;
  }
  ret += ((LL)q.size() << 32);
  return ret;
}


//! returns the winner and update the given decks
int combat(vector<deque<int>>& q, int lvl=0)
{
  // cerr << "combat lvl " << lvl << ", # of cards = " << q[0].size() << ' ' << q[1].size() << endl;

  set<pair<LL, LL>> alreadySeen;
  while (!q[0].empty() && !q[1].empty()) {
    // cerr << q[0][0] << ':' << q[0].size() << "  vs  " << q[1][0] << ':' << q[1].size() << endl;
    pair<LL, LL> hashPair = { hashQ(q[0]), hashQ(q[1]) };
    if (alreadySeen.find(hashPair) != alreadySeen.end()) {
      // cerr << "** infinite recursion detected. player-0 wins **" << endl;
      return 0;
    }
    alreadySeen.insert(hashPair);
    int v[2];
    rep(p, 2) {
      v[p] = q[p].front();
      q[p].pop_front();
    }
    int winner = (v[0] < v[1] ? 1 : 0);
    if (v[0] <= q[0].size() && v[1] <= q[1].size()) {
      //! it took ages for me to realise that we do not pass the entire sub-deck to the recursion :(
      vector<deque<int>> subQ(2);
      rep(p, 2) {
        rep(i, v[p]) subQ[p].push_back(q[p][i]);
      }
      winner = combat(subQ, lvl+1);
    }
    q[winner].push_back(v[winner]);
    q[winner].push_back(v[1-winner]);
  }

  return (q[0].empty() ? 1 : 0);
}


int main()
{
  cin.tie(0);
  ios::sync_with_stdio(0);

  int n;
  cin >> n;
  vector<deque<int>> q(2);
  rep(p, 2) {
    rep(i, n) {
      int v;
      cin >> v;
      q[p].push_back(v);
    }
  }

  combat(q);

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

