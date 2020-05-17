#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> a(n);
    for(int a_i = 0; a_i < n; a_i++){
    	cin >> a[a_i];
    }
    
    int numSwaps = 0;

    for (int i=0; i<n; i++) {
        for (int j=0; j<n-1; j++) {
            if (a[j]>a[j+1]) {
                int tmp=a[j];
                a[j]=a[j+1];
                a[j+1]=tmp;
                numSwaps++;
            }
        }
        if (numSwaps==0) break;
    }

    printf("Array is sorted in %i swaps.\n", numSwaps);
    printf("First Element: %i\n", a[0]);
    printf("Last Element: %i\n", a[a.size()-1]);

    
    return 0;
}
