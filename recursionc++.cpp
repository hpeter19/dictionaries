#progogram to demonstrate recursion in c++
#The factorial function is a recursive function that calculates the factorial of a number.
#The base case is when n == 0. According to the definition of factorial, 0! = 1, so when n is 0, the function returns 1.
#For other values of n, the function calls itself recursively: factorial(n) = n * factorial(n - 1).
#The main function asks the user for an integer and calculates the factorial using recursion.

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
#
    return 0;
}
# 