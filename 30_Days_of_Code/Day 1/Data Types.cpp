#include <iostream>
#include <iomanip>
#include <limits>

using namespace std;

int main() {
    int i = 4;
    double d = 4.0;
    string s = "HackerRank ";

    
    // Declare second integer, double, and String variables.
    int i_2;
    double  d_2;
    string s_2;

    // Read and save an integer, double, and String to your variables.
    string tmp;

    getline(cin, tmp);
    i_2 = stoi(tmp);

    getline(cin, tmp);
    d_2 = stod(tmp);


    getline(cin, s_2);

    
    // Print the sum of both integer variables on a new line.
    cout<<i+i_2<<endl;
    
    // Print the sum of the double variables on a new line.
    cout<<fixed<<setprecision(1)<<d+d_2<<endl;

    // Concatenate and print the String variables on a new line
    // The 's' variable above should be printed first.
    cout<<s+s_2<<endl;
 

    return 0;
}
