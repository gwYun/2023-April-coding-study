#include <bits/stdc++.h>

using namespace std;

vector<char> v = {'*', '-', '+'};
vector<char> opers;
vector<long long> nums; // 각 피연산자 (연산자보다 무조건 하나 더 많음)
vector<char> o; // 연산자
int vis[3];
long long ans;

long long cc(long long n1, long long n2, char opp) {
  if (opp == '*') {
    return n1 * n2;
  } else if (opp == '+') {
    return n1 + n2;
  } else {
    return n1 - n2;
  }
}

long long calculate() {
  // 우선순위 결정된 연산자들
  vector<long long> tmpn = nums; 
  vector<char> tmpo = o;

  for (char po : opers) {
    for (int i = 0; i < tmpo.size(); i++) {
      if (tmpo[i] == po) {
        tmpn[i] = cc(tmpn[i], tmpn[i + 1], po);
        tmpn.erase(tmpn.begin() + i + 1);
        tmpo.erase(tmpo.begin() + i);
        i--;
      }
    }
  }

  return abs(tmpn.front());
}

void make_expr(int idx) {
  // 각 연산자 경우의 수를 만들었을 때
  if (idx == 3) {
    long long result = calculate();

    ans = max(ans, result);

    return;
  }

  for (int i = 0; i < 3; i++) {
    if (vis[i])
      continue;
    opers.push_back(v[i]);
    vis[i] = 1;
    make_expr(idx + 1);
    opers.pop_back();
    vis[i] = 0;
  }
}

long long solution(string expression) {
  string pn;
  for (char c : expression) {
    if (c >= '0' && c <= '9') {
      pn += c;
    } else {
      nums.push_back(stoi(pn));
      o.push_back(c);
      pn = "";
    }
  }

  nums.push_back(stoi(pn));

  make_expr(0);

  return ans;
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  solution("100-200*300-500+20");

  cout << ans;

  return 0;
}
