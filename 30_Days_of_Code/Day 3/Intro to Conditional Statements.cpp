#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;

    if(N % 2 != 0) {
    cout << "Weird"<<endl;
    }    
    else {
        if (N <= 5) cout << "Not Weird"<<endl;
        else if (N <= 20) cout << "Weird"<<endl;
        else cout << "Not Weird"<<endl;
    }
}
