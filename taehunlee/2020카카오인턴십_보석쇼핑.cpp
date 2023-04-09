#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<string> gems) {

  unordered_set<string> ss;
  for (string g : gems) {
    ss.insert(g);
  }
  int n = ss.size();
  int sz = gems.size();
  ss.clear();

  int l = 0, r = 0;
  int ml = 0;
  int mr = sz;

  unordered_map<string, int> sm;
  while (1) {
    if (sm.size() == n) {
      if (mr - ml > r - l) {
        ml = l;
        mr = r;
      }

      sm[gems[l]]--;

      if (sm[gems[l]] == 0) {
        sm.erase(sm.find(gems[l]));
      }

      l++;
    } else {
      if (r == sz) {
        break;
      }
      sm[gems[r]]++;

      r++;
    }
  }
  vector<int> answer;
  // map에 사이즈 체크 하는 부분이 r은 이미 선반영되어있기때문에 ml만 +1 해준다.
  answer.push_back(ml + 1);
  answer.push_back(mr);

  return answer;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  // vector<string> input = {"DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD",
  // "SAPPHIRE", "DIA"}; 3, 7 -> 3, 8 vector<string> input = {"AA", "AB", "AC",
  // "AA", "AC"}; 1, 3 -> 1, 4 vector<string> input = {"XYZ", "XYZ", "XYZ"}; 1,
  // 1 -> 1, 2
  vector<string> input = {"ZZZ", "YYY", "NNNN", "YYY", "BBB"};
  // 1, 5 -> 1, 5

  vector<int> ans = solution(input);

  return 0;
}