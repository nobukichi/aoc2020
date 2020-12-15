#include <iostream>
#include <vector>

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

const int INF = 1001001001;
const LL INFL = 1e18;
const int MOD = 1000000007;

#define USE_ACL
#ifdef USE_ACL

#include <atcoder/all>
using namespace atcoder;

#endif


int main()
{
  cin.tie(0);
  ios::sync_with_stdio(0);

  string s;
  cin >> s;
  size_t pos = 0;
  vector<LL> r, m;
  for (int i = 0; pos < s.length(); ++i) {
    size_t next = s.find(',', pos);
    if (next == string::npos) next = s.length();
    string token = s.substr(pos, next-pos);
    if (token != "x") {
      int id = stoi(token);
      m.push_back(id);
      r.push_back(i);
    }
    pos = next+1;
  }

  pair<LL, LL> crtRes = crt(r, m);      //! This is a function to solve Chinese Remainder Theorem equation
  cout << crtRes.S - crtRes.F << endl;

  return 0;
}
