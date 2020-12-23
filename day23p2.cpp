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


//! represent the sequence with a doubly linked list
struct Node {
  int val;
  int prev;
  int next;
};


int main()
{
  const int SEQ_LEN   =  1000000;
  const int ITERATION = 10000000;

  cin.tie(0);
  ios::sync_with_stdio(0);

  string s;
  cin >> s;

  //! Setup the initial sequence of nodes
  vector<Node> node(SEQ_LEN+1);
  repr(i, 1, SEQ_LEN) node[i].val = i;
  int mx = s.length();
  rep(i, mx) {
    int curr = s[i]-'0';
    node[curr].prev = (i == 0 ? SEQ_LEN : s[i-1]-'0');
    node[curr].next = (i == mx-1 ? mx+1 : s[i+1]-'0');
  }
  repr(curr, mx+1, SEQ_LEN) {
    node[curr].prev = (curr == mx+1 ? s[mx-1]-'0' : curr-1);
    node[curr].next = (curr == SEQ_LEN ? s[0]-'0' : curr+1);
  }

  //! Run the simulation
  vector<int> pickedup(3);
  int curr = s[0]-'0';
  rep(i, ITERATION) {
    //! choose the pickedup nodes and the next current
    int p = node[curr].next;
    rep(j, 3) {
      pickedup[j] = p;
      p = node[p].next;
    }
    int nextCurr = p;

    //! find the destination and the node after the destination
    int dest = (curr == 1 ? SEQ_LEN : curr-1);
    while (find(pickedup.begin(), pickedup.end(), dest) != pickedup.end()) {
      dest = (dest == 1 ? SEQ_LEN : dest-1);
    }
    int postDest = node[dest].next;

    //! update the links
    node[curr].next = nextCurr;
    node[nextCurr].prev = curr;
    node[pickedup[0]].prev = dest;
    node[dest].next = pickedup[0];
    node[pickedup[2]].next = postDest;
    node[postDest].prev = pickedup[2];

    curr = nextCurr;
  }

  LL star1 = node[1].next;
  LL star2 = node[star1].next;
  cout << star1 << ' ' << star2 << ' ' << star1*star2 << endl;

  return 0;
}

