#include <bits/stdc++.h>

using namespace std;

int n;
int board[51][10]; // 이닝에서 선수들이 얻은 결과를 저장하는 배열
int order[10];     // 타순(순열)을 저장하는 배열
bool visited[10]; // 타순(순열) 생성에 사용되는 배열
int answer = 0;   // 최대 득점

// 이닝 진행 함수
int playGame() {
  int score = 0;                 // 현재 이닝에서 얻은 점수
  int start = 1;                 // 타자 번호
  for (int i = 1; i <= n; i++) { // 각 이닝마다
    int out = 0;                 // 아웃 수
    int b1 = 0, b2 = 0, b3 = 0;  // 1루, 2루, 3루에 있는 선수의 수
    while (out < 3) {            // 3아웃이 나올 때까지 반복
      int result = board[i][order[start]]; // 현재 타자의 결과
      if (result == 0) {                   // 아웃인 경우
        out++;
      } else if (result == 1) { // 안타인 경우
        score += b3;            // 3루에 있는 선수의 점수 추가
        b3 = b2;
        b2 = b1;
        b1 = 1;                 // 1루에 선수 추가
      } else if (result == 2) { // 2루타인 경우
        score += b2 + b3;       // 2루, 3루에 있는 선수의 점수 추가
        b3 = b1;
        b2 = 1; // 2루에 선수 추가
        b1 = 0;
      } else if (result == 3) { // 3루타인 경우
        score += b1 + b2 + b3; // 1루, 2루, 3루에 있는 선수의 점수 추가
        b1 = b2 = 0;
        b3 = 1;                    // 3루에 선수 추가
      } else {                     // 홈런인 경우
        score += b1 + b2 + b3 + 1; // 1루, 2루, 3루, 현재 타자의 점수 추가
        b1 = b2 = b3 = 0;
      }
      start = (start == 9 ? 1 : start + 1); // 타순 순환
    }
  }
  return score; // 현재 이닝에서 얻은 점수 반환
}

// 순열 생성 함수
void makeOrder(int cnt) {
  if (cnt == 10) { // 타순(순열)을 모두 생성한 경우
    answer = max(answer, playGame()); // 득점 계산
    return;
  }
  if (cnt == 4) { // 1번 선수는 4번 타자로 고정
    order[cnt] = 1;
    makeOrder(cnt + 1);
    return;
  }
  for (int i = 2; i <= 9; i++) { // 2번부터 9번 선수까지
    if (!visited[i]) {           // 아직 선택되지 않은 경우
      visited[i] = true;
      order[cnt] = i;
      makeOrder(cnt + 1);
      visited[i] = false;
    }
  }
}

int main() {
  cin >> n;
  for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= 9; j++) {
      cin >> board[i][j];
    }
  }
  makeOrder(1);           // 순열 생성
  cout << answer << endl; // 최대 득점 출력
  return 0;
}

