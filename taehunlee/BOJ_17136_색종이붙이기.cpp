#include <bits/stdc++.h>

using namespace std;

int m[10][10];
int p[5] = {5, 5, 5, 5, 5};
int ans = 2e9;

bool chk(int y, int x, int n) {
    for(int i = y; i <= y + n; i++) {
        for(int j = x; j <= x + n; j++) {
            if(i > 9 || i < 0 || j > 9 || j < 0) return false;
            if(!m[i][j]) return false;
        }
    }

    return true;
}

bool all_fill_chk() {
    for(int i = 0; i < 10; i++) {
        for(int j = 0; j < 10; j++) {
            if(m[i][j]) return false;
        }
    }

    return true;
}

void fill(int y, int x, int n) {
    for(int i = y; i <= y + n; i++) {
        for(int j = x; j <= x + n; j++) {
            m[i][j] = 0;
        }
    }
}

void unfill(int y, int x, int n) {
    for(int i = y; i <= y + n; i++) {
        for(int j = x; j <= x + n; j++) {
            m[i][j] = 1;
        }
    }
}

void solve(int cnt) {
  if (ans < cnt) {
    return;
  }

  if(all_fill_chk()) {
      ans = min(ans, cnt);
      return;
  }

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
        if(!m[i][j]) continue;

        for(int k = 4; k >= 0; k--) {
            if(!p[k]) continue;
            if(!chk(i, j, k)) continue;
            p[k]--;
            fill(i, j, k);
            solve(cnt + 1);
            unfill(i, j, k);
            p[k]++;
        }

        return;
    }
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  for (int i = 0; i < 10; i++) {
    for (int j = 0; j < 10; j++) {
      cin >> m[i][j];
    }
  }

  solve(0);

  if(ans == 2e9) {
      cout << -1;
  } else {
    cout << ans;
  }

  return 0;
}
