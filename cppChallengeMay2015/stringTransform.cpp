//https://www.hackerrank.com/contests/code-cpp-may-2015/challenges/string-transformations

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    std::string str, substr;
    int num_cases, start, end;
    cin >> str;
    cin >> num_cases;
    for(int i=0; i<num_cases; i++){
        cin >> start >> end;
        substr = str.substr(start, end+1-start);
        //cout<<"str:"<<str<<"   substr:"<<substr<<endl;
        std::reverse(std::begin(substr), std::end(substr));
        str.replace(start, end+1-start, substr);
        cout << str << endl;
    }

    return 0;
}

