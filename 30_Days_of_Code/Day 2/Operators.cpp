#include <bits/stdc++.h>

using namespace std;

// Complete the solve function below.
void solve(double meal_cost, int tip_percent, int tax_percent) {
double total_cost;
total_cost = meal_cost+(tip_percent+tax_percent)*meal_cost/100;
cout<<round(total_cost)<<endl;
}

int main()
{
    double meal_cost;
    cin >> meal_cost;

    int tip_percent;
    cin >> tip_percent;

    int tax_percent;
    cin >> tax_percent;

    solve(meal_cost, tip_percent, tax_percent);

    return 0;
}
