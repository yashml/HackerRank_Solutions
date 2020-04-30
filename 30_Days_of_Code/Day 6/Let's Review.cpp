#include <iostream>

using namespace std;


int main() {
    
    int n; 
    cin>>n;

    for(int i=0; i<n; i++){

        string str; 
        cin>>str;

        for (int j = 0; j < str.length(); j++) {
            if (j % 2 == 0) cout << str[j];
        }

        cout << " ";

        for (int k = 0; k < str.length(); k++) {
            if (k % 2 != 0) cout << str[k];
        }

        cout << endl;

    }
