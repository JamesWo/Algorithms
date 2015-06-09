//https://www.hackerrank.com/contests/code-cpp-may-2015/challenges/redundant-or-not
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
using namespace std;

int main() {
    std::unordered_map<int, int> map;
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int numCases;
    int x;
    cin >> numCases;
    for (int i=0; i<numCases; i++) {
        cin >> x;
        if (map[x]==1){
            cout << "REDUNDANT" << endl;
        } else {
            map[x]=1;
            cout << "ADDED" << endl;
        }
    }
    return 0;
}

