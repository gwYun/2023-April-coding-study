#include <bits/stdc++.h>

using namespace std;

unordered_set<long long> S;
unordered_map<long long, long long> M;

long long find_selectable_room(long long rn) {
    if(M.count(rn)) {
        M[rn] = find_selectable_room(M[rn]);
        return M[rn];
    } else {
        M[rn] = rn + 1;
        return rn;
    }
}

vector<long long> solution(long long k, vector<long long> room_number) {
    vector<long long> answer;

    for(long long rn : room_number) {
        answer.push_back(find_selectable_room(rn));
    }

    return answer;
}

int main() {
   ios::sync_with_stdio(false);
   cin.tie(NULL); cout.tie(NULL);
   long long k = 10;
   vector<long long> v = {1,3,4,1,3,1};

   solution(k, v);

   return 0;
}
