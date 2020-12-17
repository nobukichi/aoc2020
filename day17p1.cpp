#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

#define rep(i,n) for (int i = 0; i < int(n); ++i)
#define repr(i,from,to) for (int i = int(from); i <= int(to); ++i)

typedef tuple<int, int, int> P;

int main()
{
  cin.tie(0);
  ios::sync_with_stdio(0);

  int n;
  cin >> n;
  vector<string> s(n);
  rep(i, n) cin >> s[i];

  int mnx = 0, mny = 0, mnz = 0, mxx = n-1, mxy = n-1, mxz = 0;

  map<P, bool> curr;
  rep(y, n) rep(x, n) if (s[y][x] == '#') curr[{x, y, 0}] = true;

  rep(j, 6) {
    --mnx; ++mxx;
    --mny; ++mxy;
    --mnz; ++mxz;
    map<P, bool> next;
    repr(z, mnz, mxz) repr(y, mny, mxy) repr(x, mnx, mxx) {
      int an = 0;
      repr(oz, -1, 1) repr(oy, -1, 1) repr(ox, -1, 1) {
        if (oz == 0 && oy == 0 && ox == 0) continue;
        if (curr[{x+ox, y+oy, z+oz}]) ++an;
      }
      next[{x, y, z}] = ((curr[{x, y, z}] && (an == 2 || an == 3)) || (!curr[{x, y, z}] && an == 3));
    }
    curr.swap(next);
  }

  int ans = 0;
  repr(z, mnz, mxz) {
    cerr << "z = " << z << endl;
    repr(y, mny, mxy) {
      repr(x, mnx, mxx) {
        if (curr[{x, y, z}]) ++ans;
        cerr << (curr[{x, y, z}] ? '#' : '.');
      }
      cerr << endl;
    }
  }
  cout << ans << endl;

  return 0;
}
