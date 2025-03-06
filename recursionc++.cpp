#progogram to demonstrate recursion in c++

#include<iostream>
using namespace std;

// Function to calculate factorial using recursion
int factorial(int n) {
    // Base case: if n is 0, return 1 (since 0! = 1)
    if (n == 0) {
        return 1;
    }
    // Recursive case: factorial of n is n * factorial of (n-1)
    else {
        return n * factorial(n - 1);
    }
}

int main() {
    int num;
    
    cout << "Enter a number: ";
    cin >> num;

    // Calculate factorial using recursion
    int result = factorial(num);

    cout << "The factorial of " << num << " is: " << result << endl;

    return 0;
}
