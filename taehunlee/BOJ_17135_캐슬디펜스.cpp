#include <bits/stdc++.h>

using namespace std;

int N, M, D;
int mm[16][16];
int tmp[16][16];
int k[16][16];

vector<int> ap;
int vis[16];
int ans;

struct Node {
  int x, y, d;
  bool operator()(const Node n1, const Node n2) const {
    if (n1.d == n2.d)
      return n1.y > n2.y;
    else
      return n1.d > n2.d;
  }
};

void kill() {
  int tmp[16][16];
  int cnt = 0;
  int loop = N;
  memcpy(tmp, mm, sizeof(mm));
  while (loop--) {
    vector<Node> v;
    for (int k = 0; k < 3; k++) {
      priority_queue<Node, vector<Node>, Node> q;
      for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
          if (tmp[i][j]) {
            int dist = abs(N - i) + abs(ap[k] - j);
            if (dist <= D)
              q.push({i, j, dist});
          }
        }
      }
      if (q.size()) {
        int x = q.top().x, y = q.top().y;
        v.push_back({x, y});
      }
    }

    for (int i = 0; i < v.size(); i++) {
      int x = v[i].x, y = v[i].y;
      if (tmp[x][y]) {
        tmp[x][y] = 0;
        cnt += 1;
      }
    }

    for(int i = N - 1; i >= 1; i--) {
        for(int j = 0; j < M; j++) {
            tmp[i][j] = tmp[i - 1][j];
        }
    }

    for (int i = 0; i < M; i++)
      tmp[0][i] = 0;
  }

  ans = max(ans, cnt);
}

void make_pos(int idx) {
  if (idx == 3) {
    kill();
  }

  for (int i = 0; i < M; i++) {
    if (vis[i])
      continue;
    if (!ap.empty() && ap.back() < i)
      continue;
    vis[i] = 1;
    ap.push_back(i);
    make_pos(idx + 1);
    ap.pop_back();
    vis[i] = 0;
  }
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  cin >> N >> M >> D;

  for (int i = 0; i < N; i++) {
    for (int j = 0; j < M; j++) {
      cin >> mm[i][j];
    }
  }

  make_pos(0);

  cout << ans;

  return 0;
}
