#include <bits/stdc++.h>

using namespace std;

int S[100001];
vector<pair<int, int>> V;

vector<int> solution(string s) {
  vector<int> answer;

  string cs;
  vector<int> vv;
  for (int i = 0; i < s.size(); i++) {
    char cc = s[i];
    if (cc >= '0' && cc <= '9') {
      cs += cc;
    } else {
      if (cs.size() == 0)
        continue;

      int cn = stoi(cs);
      vv.push_back(cn);

      if (cc == '}') {
        int vvs = vv.size();

        for (int _n : vv) {
          // if(S.count(_n)) continue;
          // S.insert(_n);
          V.push_back({vvs, _n});
        }

        vv.clear();
      }

      cs = "";
    }
  }

  sort(V.begin(), V.end());

  for (pair<int, int> p : V) {
    if (S[p.second])
      continue;
    S[p.second]++;
    answer.push_back(p.second);
  }

  return answer;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  // (1, 2), (2, 1), (3, 3), (4, 4)
  //    string input = "{{2},{2,1},{2,1,3},{2,1,3,4}}"; // -> {2, 1, 3, 4}
  //   string input = "{{1,2,3},{2,1},{1,2,4,3},{2}}"; // -> {2, 1, 3, 4}
  string input = "{{20,111},{111}}";

  solution(input);

  return 0;
}
