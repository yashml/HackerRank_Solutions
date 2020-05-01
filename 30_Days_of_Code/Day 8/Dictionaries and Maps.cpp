#include <map>
#include <iostream>

using namespace std;

int main() {
    int n;
    string name;
    cin>>n;

    map<string, int> phonebook;

    for (int i = 0; i < n; i++) {
        cin>>name;

        if (!phonebook[name]) {
            cin>>phonebook[name];
        }
    }

    while (cin>>name) {

        if (phonebook[name]) {
            cout<<name<<"="<<phonebook[name]<<endl;

        } else {
            cout<<"Not found"<<endl;
        }
    }

    return 0;
}
