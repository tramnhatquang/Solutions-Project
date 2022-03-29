#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

template <typename T>
void printArray(vector<T> vec) {
    for (int  i= 0; i < vec.size(); i++) {
        cout << vec[i] << endl;
    }
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int num;
    cin >> num;

    vector<int> vec(num);
    for (int  i =0; i < num; i++)
    {
        int input;
        cin >> input;
        vec[i] = input;
    }
    printArray(vec);

    int num_string;
    cin >> num_string;
    vector<string> vec1(num_string);
    for (int  i =0; i < num_string; i++)
    {
        string input;
        cin >> input;
        vec1[i] = input;
    }
    printArray(vec1);



    return 0;
}
