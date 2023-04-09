#include <bits/stdc++.h>

using namespace std;

/**
 * https://school.programmers.co.kr/learn/courses/30/lessons/67259
 */

// 위, 오, 아, 왼
int dy[4] = { -1, 0, 1, 0 };
int dx[4] = { 0, 1, 0, -1 };
int ans = 2e9;

int solve(vector<vector<int>> &board) {
    int N = board.size();
    int v[26][26][4]; // TODO 방향 배열 2개로 줄이기
    memset(v, 0x3f3f3f3f, sizeof(v));

    queue<tuple<int, int, int, int>> q;

    /**
     * i
     * 0: 위, 1: 오, 2: 아, 3: 왼
     */
    for(int i = 0; i < 4; i++) {
        v[0][0][i] = 0;
    }
    q.push({0, 0, 4, 0});

    while(!q.empty()) {
        auto [y, x, dir, sum] = q.front();
        q.pop();

        if(y == N - 1 && x == N - 1) {
            for(int i = 0; i < 4; i++) {
                ans = min(ans, v[N - 1][N - 1][i]);
            }
        }

        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if(ny < 0 || ny > N - 1 || nx < 0 || nx > N - 1) continue;
            if(board[ny][nx]) continue;

            int nw = 100;
            if((dir == 0 || dir == 2) && (i == 1 || i == 3)) {
                nw += 500;
            }
            if((dir == 1 || dir == 3) && (i == 0 || i == 2)) {
                nw += 500;
            }

            int tw = sum + nw;

            if(v[ny][nx][i] <= tw) continue;
            v[ny][nx][i] = tw;

            q.push({ny, nx, i, tw});
        }
    }

    return ans;
}

int solution(vector<vector<int>> board) {
    return solve(board);
}